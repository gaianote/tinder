from flask import Flask, redirect, url_for
from flask_socketio import SocketIO

from tinder.common.server import ThreadServer

from .apis import api

"""
Mock server

tinder main server
Default port : 9090

* HTTP mock
* HTTP record
* tinder UI
* tinder API
* tinder plugin management
"""


class WebServer(ThreadServer):
    """
    模拟接口服务
    使用flask在默认的9090端口启动，模拟线上接口，同时支持通过api动态修改接口数据。

    """

    def __init__(self):
        super().__init__()
        self.debug = True
        self.port = 9090
        self._working_thread = None
        self.app = Flask("MOCK")
        self.app.env = "development"

        # async_mode = threading / eventlet / gevent / gevent_uwsgi
        self.socket_io = SocketIO(
            self.app, async_mode="threading", logger=False, cors_allowed_origins="*"
        )

        # 存储socket-io
        # context.application.socket_io = self.socket_io
        # application._socketio = self.socket_io

        # Register blueprints
        self.app.register_blueprint(api)
        # self.app.register_blueprint(core)
        # self.app.register_blueprint(ui)

        # @self.app.route("/")
        # def index():
        #     """
        #     设置默认页面为UI首页
        #     """
        #     return redirect(url_for("ui.index") + f"?v={VERSION}")

    def run(self):
        self.socket_io.run(
            self.app,
            host="0.0.0.0",
            port=self.port,
            debug=self.debug,
            use_reloader=False,
        )

    def stop(self):
        """
        停止服务

        """
        super().stop()
        try:
            self.socket_io.stop()
        except Exception:
            pass
