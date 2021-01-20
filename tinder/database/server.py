import datetime
import json
import math
import time
import traceback
from pathlib import Path
from queue import Queue

from sqlalchemy import Column, DateTime, Integer, String, Text, create_engine, event, Boolean, UnicodeText
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import scoped_session, sessionmaker
from contextlib import contextmanager
from tinder.common.server import ThreadServer

Base = declarative_base()


class TinderDatabaseServer(ThreadServer):

    def __init__(self, path=None):
        super().__init__()

        if not path or path.isspace():
            ROOT_DIR = Path('~/.tinder').expanduser()
            DEFAULT_NAME = 'tinder.db'
            database_uri = ROOT_DIR / DEFAULT_NAME
        else:
            path_obj = Path(path).expanduser()
            if path_obj.is_absolute():
                database_uri = path_obj
            else:
                database_uri = path_obj.absolute()
        print(database_uri)

        sqlite_path = 'sqlite:///' + \
            str(database_uri) + '?check_same_thread=False'

        engine = create_engine(str(sqlite_path))
        # event.listen(engine, 'connect', self._fk_pragma_on_connect)
        Base.metadata.create_all(engine)
        session_factory = sessionmaker(bind=engine)
        Session = scoped_session(session_factory)
        self._scoped_session = Session

    # def _fk_pragma_on_connect(self, dbapi_con, con_record):
    #     # https://www.sqlite.org/pragma.html#pragma_journal_mode
    #     dbapi_con.execute('PRAGMA journal_mode=MEMORY')
    #     # https://www.sqlite.org/pragma.html#pragma_synchronous
    #     dbapi_con.execute('PRAGMA synchronous=OFF')
    # def run(self):
    #     session = self._scoped_session()
    #     while self.running:
    #         try:
    #             event = self.storage_queue.get()
    #             session.add(event)
    #             session.commit()
    #         except Exception:
    #             logger.error(f'Save event failed. {traceback.format_exc()}')

    # def stop(self):
    #     super().stop()

    @property
    def session(self):
        return self._scoped_session()

    @contextmanager
    def session_maker(self):
        try:
            yield self.session
            self.session.commit()
        except:
            self.session.rollback()
            raise
        finally:
            self.session.close()

    def serialize(self, models, keys=None):
        from sqlalchemy.orm import class_mapper

        if type(models) == list:
            result = []
            for model in models:
                if keys:
                    columns = keys
                else:
                    columns = [c.key for c in class_mapper(model.__class__).columns]
                result.append(dict((c, getattr(model, c)) for c in columns))
            return result
        else:
            if keys:
                columns = keys
            else:
                columns = [c.key for c in class_mapper(models.__class__).columns]
            return dict((c, getattr(models, c)) for c in columns)


class MapRemoteConifgTable(Base):
    """
    map 表
    """
    __tablename__ = 'map_remote_config'

    id = Column(Integer, primary_key=True, autoincrement=True)
    map_from = Column(Text)
    map_to = Column(Text)
    enable = Column(Boolean)  # false 关闭映射 true 开启映射
    rid = Column(Text)


class MockRulesConifgTable(Base):
    """
    mock 规则表
    """
    __tablename__ = 'mock_rule_config'

    rule = Column(Text)  # 匹配规则 默认为 url
    request = Column(Text)
    response = Column(Text)
    group_name = Column(Text)
    describe = Column(Text)
    enable = Column(Boolean)  # false 关闭映射 true 开启映射
    rid = Column(Text, primary_key=True)


db = TinderDatabaseServer()
