import json
import time
import weakref
import re
from tinder.common import catch
from tinder.database.server import db, MapRemoteConifgTable
from tinder.controller.map_remote import MapRemoteController
from tinder.controller.mock import MockRulesController
import socket


def get_ip():
    """
        Get local ip from socket connection

        :return: IP Addr string
        """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('bing.com', 80))
    return s.getsockname()[0]


local_ip = get_ip()


class ProxyManger():
    def __init__(self, flow):
        self.catch = catch.get_cache()
        self.flow = flow
        self.local_ip = local_ip

    # def recode():

    @property
    def is_local_request(self):
        """
        如果是tinder宿主机对于tinder服务器发出的请求,直接忽略
        """
        if self.flow.request.host in ["localhost", "127.0.0.1", self.local_ip] and self.flow.request.port in [9090, 8081]:
            return True
        else:
            return False

    def mock(self):
        """
        """
        rules = MockRulesController.get_rule_list(enable=True)
        for rule in rules:
            if re.match(rule["rule"], self.flow.request.url):
                target = MockRulesController.get_rule_detail(rule["rid"])
                self.flow.response.headers["tinder"] = "mock"
                res = json.loads(json.loads(target["response"]))["data"]
                self.flow.response.set_text(json.dumps(res, ensure_ascii=False))

    def serialize(self, target):
        data = {}
        for key in target.keys():
            data[key] = target[key]
        return data

    def get_time(self, timestamp):
        """
        时间戳转时间
        """
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))

    def handle_request(self):
        if not self.is_local_request:
            self.map_remote()
            self.catch.add(self.flow)

    def handle_response(self):
        self.mock()

    def map_remote(self):
        map_rule_list = MapRemoteController.get_rule_list()

        def resolve_url(url):
            port = None
            rule = r"([a-z][a-z0-9+\-.]*)://([a-z0-9\-._~%]+|\[[a-z0-9\-._~%!$&'()*+,;=:]+\])(:[0-9]+)?([a-zA-Z0-9\-\/._~%!$&'()*+]+)?(\?[a-zA-Z0-9&=]+)?"
            scheme, host, path, param, port = re.findall(rule, url)[0]
            if not port:
                if scheme == "https":
                    port = "443"
                if scheme == "http":
                    port = "80"

            return scheme, host, path, param, int(port)
        for map_rule in map_rule_list:
            if map_rule["enable"] == True:
                if self.flow.request.url.startswith(map_rule["map_from"]):
                    scheme, host, path, param, port = resolve_url(map_rule["map_to"])
                    self.flow.request.scheme = scheme
                    self.flow.request.host = host
                    self.flow.request.headers["Host"] = host
                    self.flow.request.port = port
                    self.flow.request.path = path + self.flow.request.path
