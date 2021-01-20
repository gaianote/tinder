from tinder.proxy.server import ProxyServer
from tinder.web.server import WebServer


def main():
    webserver = WebServer()
    proxyserver = ProxyServer()
    webserver.start()
    proxyserver.start()


if __name__ == "__main__":
    main()
