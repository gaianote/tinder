import json
import time
from collections import deque

_cache = None


def serialize(target):
    data = {}
    for key in target.keys():
        data[key] = target[key]
    return data


def get_time(timestamp):
    """
    时间戳转时间
    """
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))


def get_cache():
    global _cache
    if not _cache:
        _cache = ListCache()
    return _cache


def flow_to_json(flow):
    flow_json = {
        "size": 0,
        "duration": 0,
        "status": 0,
        "id": flow.id,
        "start": get_time(int(flow.request.timestamp_start)),
        "url": flow.request.url.split("?")[0],
        "method": flow.request.method,
        "request": {
            "host": flow.request.host,
            "url": flow.request.url.split("?")[0],
            "path": flow.request.path.split("?")[0],
            "port": flow.request.port,
            "method": flow.request.method,
            "scheme": flow.request.scheme,
            "data": serialize(flow.request.urlencoded_form),
            "query": serialize(flow.request.query),
            "headers": serialize(flow.request.headers),
        }
    }

    if flow.response and flow.response.content:
        try:
            response_data = json.loads(flow.response.text)
        except:
            try:
                response_data = flow.response.text
            except:
                response_data = "TinderParseError: can not decode response"
        flow_json["size"] = len(flow.response.content)
        flow_json["duration"] = int((flow.response.timestamp_end
                                     - flow.request.timestamp_start) * 1000)
        flow_json["status"] = flow.response.status_code
        flow_json["response"] = {
            "code": flow.response.status_code,
            "headers": serialize(flow.response.headers),
            "data": response_data,
        }
    return flow_json

    # flow_json = {
    #     "size": len(flow.response.content),
    #     "duration": int((flow.response.timestamp_end
    #                      - flow.request.timestamp_start) * 1000),
    #     "id": flow.id,
    #     "start": get_time(int(flow.request.timestamp_start)),
    #     "url": flow.request.url,
    #     "method": flow.request.method,
    #     "status": flow.response.status_code,
    #     "request": {
    #         "host": flow.request.host,
    #         "url": flow.request.url,
    #         "path": flow.request.path.split("?")[0],
    #         "port": flow.request.port,
    #         "method": flow.request.method,
    #         "scheme": flow.request.scheme,
    #         "data": serialize(flow.request.urlencoded_form),
    #         "query": serialize(flow.request.query),
    #         "headers": serialize(flow.request.headers),
    #     },
    #     "response": {
    #         "code": flow.response.status_code,
    #         "headers": serialize(flow.response.headers),
    #         "data": json.loads(flow.response.text),
    #     },
    # }


class ListCache:
    """
    双向序列
    默认最大值1000
    存储流经mock服务的数据

    """

    def __init__(self, maxlen=1000):
        self._cache = deque(maxlen=maxlen)

    def add(self, obj):
        self._cache.appendleft(obj)

    def items(self):
        return [flow_to_json(flow) for flow in list(self._cache)]

    def clear(self):
        self._cache.clear()

    def delete(self, obj):
        self._cache.remove(obj)

    def delete_by_ids(self, *ids):
        del_items = []
        for item in list(self._cache):
            if item["id"] in ids:
                del_items.append(item)
        for item in del_items:
            self.delete(item)

    # def update(self, origin_obj, target_obj):
    #     index = self._cache.index(origin_obj)
    #     self._cache[index] = target_obj
