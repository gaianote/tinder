import json
import time
import weakref

from tinder.common import catch


class ProxyManger():
    def __init__(self, flow):
        self.catch = catch.get_cache()
        self.flow = flow

    # def recode():

    def mock(self):
        pass
        # if self.flow.request.host.endswith("thor.weidian.com"):
        #     self.flow.request.scheme = "http"
        #     self.flow.request.port = 80
        #     # self.flow.request.host = "houtu.vdian.net"
        #     # self.flow.request.path = "/thorRemote" + self.flow.request.path
        #     # self.flow.request.headers["Host"] = "houtu.vdian.net"
        #     self.flow.request.host = "thor.daily.weidian.com"
        #     self.flow.request.headers["Host"] = "thor.daily.weidian.com"

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
        self.mock()
        self.catch.add(self.flow)

    def handle_response(self):
        pass

        # def handle_response(self, self.flow):
        #     hit_datas = context.application.data_manager.get_matched_data(
        #         self.flow._current_req_data)
        #     if len(hit_datas) <= 0:
        #         return
        #     hit_data = hit_datas[0]
        #     self.flow.response.text = hit_data['response']['data']
        #     # headers
        #     self.flow._current_req_data["response"]["headers"]["tinder"] = "mock"
        #     self.flow._current_req_data["response"]["headers"]["isMocked"] = "True"
        #     self.flow.response.headers["tinder"] = "mock"
        #     self.flow.response.headers["isMocked"] = "True"
