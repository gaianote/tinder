import json
from contextlib import contextmanager
from tinder.database.server import db, MockRulesConifgTable
import uuid
import json


class MockRulesController:
    """
    远程映射功能支持
    """

    @staticmethod
    def get_rule_list(enable=None):
        """
        获得所有配置
        """
        # db = application.server["db"]
        if enable != None:
            result = db.session.query(
                MockRulesConifgTable
            ).filter(MockRulesConifgTable.enable == enable).all()
        else:
            result = db.session.query(
                MockRulesConifgTable
            ).all()
        return db.serialize(result, keys=["rid", "rule", "describe", "group_name", "enable"])

    @staticmethod
    def get_rule_detail(rid):
        """
        获得所有配置
        """
        # db = application.server["db"]
        result = db.session.query(MockRulesConifgTable).filter(
            MockRulesConifgTable.rid == rid).one()
        return db.serialize(result)

    @staticmethod
    def add_rule(rule: str, request: str, response: str, group_name: str, describe: str, enable: bool):
        """
        增加配置
        """
        # db = application.server["db"]
        rid = str(uuid.uuid1())
        with db.session_maker() as session:
            session.add(
                MockRulesConifgTable(
                    rid=rid, rule=rule, request=json.dumps(request), response=json.dumps(response), group_name=group_name, describe=describe, enable=enable)
            )
        return {"status": 0}

    @staticmethod
    def delete_rule(rid: str):
        """
        删除配置
        """
        with db.session_maker() as session:
            session.query(MockRulesConifgTable).filter(
                MockRulesConifgTable.rid == rid
            ).delete()
        return {"status": 0}

    @staticmethod
    def update_rule(rid: str, rule: str, request: str, response: str, group_name: str, describe: str, enable: bool):
        """
        更新配置
        """
        with db.session_maker() as session:
            mock_rule = (
                session.query(MockRulesConifgTable)
                .filter(MockRulesConifgTable.rid == rid)
                .one()
            )
            mock_rule.rule = rule
            mock_rule.request = request
            mock_rule.response = response
            mock_rule.group_name = group_name
            mock_rule.descrip = describe
            mock_rule.enable = enable
        return {"status": 0}

    @staticmethod
    def enable_rule(rid: str, enable: bool):
        """
        更新配置
        """
        with db.session_maker() as session:
            mock_rule = (
                session.query(MockRulesConifgTable)
                .filter(MockRulesConifgTable.rid == rid)
                .one()
            )
            mock_rule.enable = enable
        return {"status": 0}
