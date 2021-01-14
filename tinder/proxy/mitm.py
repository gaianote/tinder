from mitmproxy import http

from tinder.proxy.handle import ProxyManger


def request(flow: http.HTTPFlow):
    manger = ProxyManger(flow)
    manger.handle_request()


def response(flow: http.HTTPFlow):
    manger = ProxyManger(flow)
    manger.handle_response()

    # if flow.request.url.find("query") != -1:

    #     print(flow.request.url)
    #     print(response_flow)
    #     flow.response.set_text('''{
    #         "result": {
    #             "appQrCode": null,
    #             "authorizeUrl": "https://mp.weixin.qq.com/wxawap/fastregistertpbeta?action=show&create_token=flXM0QtwAF1v6OGUad_duiV7V8TszZFudYSTqCBkBybx9C13QajIg9AtPXFkg1RM#wechat_redirect",
    #             "createToken": "flXM0QtwAF1v6OGUad_duiV7V8TszZFudYSTqCBkBybx9C13QajIg9AtPXFkg1RM",
    #             "headUrl": "https://si.geilicdn.com/trial1528200009-1ecd00000176dc5c16590a219838_695_753.jpg",
    #             "leftTime": 201058,
    #             "name": "食梦者",
    #             "requestQrCode": "https://si.geilicdn.com/wxapi-1ecf00000176dc5c32c00a219838-unadjust_500_500.png",
    #             "status": 7,
    #             "statusDesc": "on trial"
    #         },
    #         "status": {
    #             "code": 0,
    #             "description": "",
    #             "message": "OK"
    #         }
    #     }''')
    # print(_catch.items()[-1])
    if flow.request.url.find("user.getRegisterInfo") != -1:

        flow.response.set_text('''{
                "status": {
                    "code": 0,
                    "message": "OK",
                    "description": ""
                },
                "result": {
                    "companyCode": "91330104MA27WYQ77B",
                    "companyCodeType": 1,
                    "companyName": "杭州基育科技有限公司",
                    "id": 1029,
                    "mobile": "13148474587",
                    "reason": "",
                    "status": 5,
                    "userName": "钱俊杰",
                    "wechatId": "qianjunjie-liuxue",
                    "showNick":true
                }
            }''')
