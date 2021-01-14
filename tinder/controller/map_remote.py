import json
from contextlib import contextmanager
from tinder.database.server import db, MapRemoteConifgTable
import uuid


@contextmanager
def session_maker(session):
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


def serialize(models):
    from sqlalchemy.orm import class_mapper

    if type(models) == list:
        result = []
        for model in models:
            columns = [c.key for c in class_mapper(model.__class__).columns]
            result.append(dict((c, getattr(model, c)) for c in columns))
        return result
    else:
        columns = [c.key for c in class_mapper(models.__class__).columns]
        return dict((c, getattr(models, c)) for c in columns)


class MapRemoteController:
    """
    远程映射功能支持
    """

    @staticmethod
    def get_rule_list():
        """
        获得所有配置
        """
        # db = application.server["db"]
        result = db.session.query(MapRemoteConifgTable).all()
        return serialize(result)

    @staticmethod
    def add_rule(map_from: str, map_to: str, enable: bool):
        """
        增加配置
        """
        # db = application.server["db"]
        rid = str(uuid.uuid1())
        with session_maker(db.session) as session:
            session.add(
                MapRemoteConifgTable(
                    map_from=map_from, map_to=map_to, enable=enable, rid=rid)
            )
        return {"status": 0}

    @staticmethod
    def delete_rule(rid: str):
        """
        删除配置
        """
        with session_maker(db.session) as session:
            session.query(MapRemoteConifgTable).filter(
                MapRemoteConifgTable.rid == rid
            ).delete()
        return {"status": 0}

    @staticmethod
    def update_rule(rid: str, map_from: str, map_to: str, enable: bool):
        """
        更新配置
        """
        with session_maker(db.session) as session:
            rule = (
                session.query(MapRemoteConifgTable)
                .filter(MapRemoteConifgTable.rid == rid)
                .one()
            )
            rule.map_from = map_from
            rule.map_to = map_to
            rule.enable = enable
        return {"status": 0}
