import json
from contextlib import contextmanager

# from tinder import application
# from tinder.db.database_server import MapRemoteConifgTable


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
        db = application.server["db"]
        result = db.session.query(MapRemoteConifgTable).all()
        return serialize(result)

    @staticmethod
    def add_rule(map_from: str, map_to: str, enable: int):
        """
        增加配置
        """
        db = application.server["db"]
        with session_maker(db.session) as session:
            session.add(
                MapRemoteConifgTable(map_from=map_from, map_to=map_to, enable=enable)
            )
        return {"status": 0}

    @staticmethod
    def delete_rule(rid: int):
        """
        删除配置
        """
        db = application.server["db"]
        with session_maker(db.session) as session:
            session.query(MapRemoteConifgTable).filter(
                MapRemoteConifgTable.id == rid
            ).delete()
        return {"status": 0}

    @staticmethod
    def update_rule(rid: int, map_from: str, map_to: str, enable: int):
        """
        更新配置
        """
        db = application.server["db"]
        with session_maker(db.session) as session:
            rule = (
                session.query(MapRemoteConifgTable)
                .filter(MapRemoteConifgTable.id == rid)
                .one()
            )
            rule.map_from = map_from
            rule.map_to = map_to
            rule.enable = enable
        return {"status": 0}
