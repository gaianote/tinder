from flask import request
from flask_restful import Resource

from tinder.common.catch import get_cache


class Flow(Resource):
    """
    http 接口获取和删除
    """

    def get(self):
        page_num = int(request.args["page_num"]) - 1
        page_size = int(request.args["page_size"])
        catch = get_cache()
        return {"status": 0, "result": catch.items()[page_num * page_size:page_size]}

    def delete(self):
        catch = get_cache()
        if not request.json["ids"]:
            catch.clear()
        else:
            catch.delete_by_ids(request.json["ids"])
        return {"status": 0}
