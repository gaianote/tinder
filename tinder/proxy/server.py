import socket
from pathlib import Path

from colorama import Fore, Style
from mitmproxy.tools.cmdline import mitmdump
from mitmproxy.tools.dump import DumpMaster

from tinder.common.server import ThreadServer

from .mitm_runer import run

"""
HTTP proxy server

Default port 8080
"""

CURRENT_PATH = Path(__file__).parent
FLOW_PATH = CURRENT_PATH / 'mitm.py'


class ProxyServer(ThreadServer):

    def __init__(self):
        super().__init__()
        self.proxy_port = "8080"

    def run(self):
        mitm_arguments = [
            '-s', str(FLOW_PATH),
            '-p', self.proxy_port,
            '--ssl-insecure',
            '--no-http2',
            '-q'
        ]

        run(DumpMaster, mitmdump, mitm_arguments)


# def info_msg(*msg):
#     print(f'{Fore.YELLOW}[proxy_server]', *msg, Style.RESET_ALL)
