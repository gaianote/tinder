import json
from flask import request
from flask_restful import Resource
from tinder.controller.mock import MockRulesController


class MockRule(Resource):
    """
    远程映射功能支持
    """

    def get(self):
        if request.args.get("rid"):
            rid = request.args.get("rid")
            result = MockRulesController.get_rule_detail(rid)
        else:
            result = MockRulesController.get_rule_list()
        return {"status": 0, "result": result}

    def post(self):
        rule = json.loads(request.data)["rule"]
        requests = json.loads(request.data)["request"]
        enable = json.loads(request.data)["enable"]
        response = json.loads(request.data)["response"]
        group_name = json.loads(request.data)["group_name"]
        describe = json.loads(request.data)["describe"]
        MockRulesController.add_rule(
            rule, requests, response, group_name, describe, enable)
        return {"status": 0}

    def put(self):
        rid = json.loads(request.data)["rid"]
        enable = json.loads(request.data)["enable"]

        if json.loads(request.data).get("request"):
            rule = json.loads(request.data)["rule"]
            requests = json.loads(request.data)["request"]
            response = json.loads(request.data)["response"]
            group_name = json.loads(request.data)["group_name"]
            describe = json.loads(request.data)["describe"]
            MockRulesController.update_rule(
                rid, rule, requests, response, group_name, describe, enable)
        else:
            MockRulesController.enable_rule(
                rid, enable)
        return {"status": 0}

    def delete(self):
        rid = json.loads(request.data)["rid"]
        MockRulesController.delete_rule(rid)
        return {"status": 0}
