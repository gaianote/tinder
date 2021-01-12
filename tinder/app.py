from tinder.proxy.server import ProxyServer
from tinder.web.server import WebServer


def main():
    webserver = WebServer()
    proxyserver = ProxyServer()
    webserver.start()
    proxyserver.start()
    print("hello world!")


if __name__ == "__main__":
    main()
