import os


class ClientProxyManager(object):
    """
    设置本机代理
    """

    def isOpen(self):
        """
        是否打开
        """
        cmd = "networksetup -getwebproxy Wi-Fi"
        result = os.popen(cmd).read()
        print(result)
        if result.find("Yes") != -1:
            return True
        else:
            return False

    def set(self):
        """
        设置代理
        """
        cmds = ["networksetup -setwebproxy Wi-Fi 127.0.0.1 8080",
                "networksetup -setsecurewebproxy Wi-Fi 127.0.0.1 8080",
                "networksetup -setsocksfirewallproxy Wi-Fi 127.0.0.1 8080"]

        for cmd in cmds:
            r = os.system(cmd)

    def open(self):
        """
        打开代理
        """
        cmds = ["networksetup -setwebproxystate Wi-Fi on",
                "networksetup -setsecurewebproxystate Wi-Fi on",
                "networksetup -setsocksfirewallproxystate Wi-Fi on"]
        for cmd in cmds:
            r = os.system(cmd)

    def close(self):
        """
        关闭代理
        """
        cmds = ["networksetup -setwebproxystate Wi-Fi off",
                "networksetup -setsecurewebproxystate Wi-Fi off",
                "networksetup -setsocksfirewallproxystate Wi-Fi off"]
        for cmd in cmds:
            r = os.system(cmd)
