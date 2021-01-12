import json

from flask import request
from flask_restful import Resource

from tinder.controller.map_remote import MapRemoteController


class MapRemote(Resource):
    """
    远程映射功能支持
    """

    def get(self):
        result = MapRemoteController.get_rule_list()
        return {"status": 0, "result": result}

    def post(self):
        map_from = json.loads(request.data)["map_from"]
        map_to = json.loads(request.data)["map_to"]
        enable = json.loads(request.data)["enable"]
        MapRemoteController.add_rule(map_from, map_to, enable)
        return {"status": 0}

    def put(self):
        map_from = json.loads(request.data)["map_from"]
        map_to = json.loads(request.data)["map_to"]
        rid = json.loads(request.data)["id"]
        enable = json.loads(request.data)["enable"]
        MapRemoteController.update_rule(rid, map_from, map_to, enable)
        return {"status": 0}

    def delete(self):
        rid = json.loads(request.data)["id"]
        MapRemoteController.delete_rule(rid)
        return {"status": 0}
