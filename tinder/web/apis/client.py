from flask import request
from flask_restful import Resource

from tinder.proxy.client import ClientProxyManager


class ClientProxy(Resource):
    """
    本地 打开/关闭 代理功能
    """

    def get(self):
        manager = ClientProxyManager()
        result = manager.isOpen()
        return {"status": 0, "result": result}

    def put(self):
        status = request.json["status"]
        manager = ClientProxyManager()
        if status == True:
            manager.set()
            manager.open()
        else:
            manager.close()
        return {"status": 0}
