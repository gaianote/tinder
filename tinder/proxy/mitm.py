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
    if flow.request.url.find("wx.queryRegisterInfo") != -1:

        flow.response.set_text('''{
            "status": {
            "code": 0,
            "message": "OK",
            "description": ""
            },
            "result": {
            "appQrCode": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAMCAgMCAgMDAwMEAwMEBQgFBQQEBQoHBwYIDAoMDAsKCwsNDhIQDQ4RDgsLEBYQERMUFRUVDA8XGBYUGBIUFRT/wAALCAG4AbgBAREA/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/9oACAEBAAA/AP1Tooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooor+Veiiiiiiv6qKKKK/lXr+qiiiv5V6/qor+Vev6qKK/lXr+qiv5V6/qooor+Vev6qK/lXoor+qiiv5V6/qor+Vev6qKKKK/lXr+qiv5V6KKKKKK/qoooooor+Vev6qKKKKK/lXr+qiiv5V6K/qor+Veiv6qKK/lXor+qiiv5V6KKKK/qooor+Vev6qKKK/lXr+qiv5V6/qor+Veiiiiv6qK/lXr+qiiiiiv5V6/qoooooor+Vev6qK/lXoor+qiv5V6/qor+Veiv6qK/lXoor+qiiiv5V6KK/qor+Veiv6qK/lXr+qiv5V6KK/qooor+Veiiiiv6qKK/lXor+qiv5V6/qor+Veiiv6qK/lXr+qiiiiiiv5V6/qor+Veiiv6qK/lXr+qiiv5V6KKKK/qor+Veiv6qKKK/lXoor+qiiiv5V6/qoor+Vev6qK/lXr+qiiv5V6/qoor+Vev6qK/lXr+qiiv5V6/qor+Veiiv6qK/lXr+qiiiiiiv5V6/qor+Veiiv6qK/lXr+qiv5V6/qoooor+Vev6qKKK/lXor+qiiv5V6KKKKKK/qoor+Vev6qKK/lXr+qiiv5V6/qooooor+Vev6qK/lXoor+qiv5V6/qoooooor+Vev6qKKKKK/lXr+qiv5V6/qor+Veiv6qK/lXoor+qiiv5V6/qor+Veiiv6qKKK/lXr+qiv5V6K/qoor+Veiiv6qK/lXoor+qiiiv5V6/qooooor+Vev6qKKKKKK/lXoooooor+qiv5V6/qor+Vev6qK/lXr+qiv5V6/qor+Vev6qK/lXr+qiv5V6/qor+Vev6qK/lXr+qiv5V6/qor+Vev6qK/lXr+qiv5V6/qor+Vev6qK/lXr+qiv5V6/qor+Vev6qK/lXoooooor+qiiiiiiiiiiiiiiiv5V6KK/qor+Veiiiiv6qK/lXr+qiv5V6K/qooor+Vev6qKK/lXr+qiiiv5V6/qor+Vev6qKKKKKKKKKKKKKKKKKKKK/lXr+qiiv5V6/qor+Vev6qK/lXooor+qiiiiiv5V6K/qoor+Veiiiiiiiv6qKKKKKK/lXr+qiv5V6K/qor+Veiv6qK/lXor+qiv5V6/qoooooooor+Veiv6qK/lXr+qiv5V6/qor+Veiv6qKKKKKK/lXoor+qiv5V6K/qoor+Veiiv6qKK/lXooor+qiiiiiv5V6KK/qoor+Vev6qK/lXr+qiiv5V6/qooooooor+Veiv6qK/lXor+qiv5V6KKKKK/qoor+Veiv6qKK/lXor+qiv5V6KK/qor+Vev6qKKK/lXooor+qiiiv5V6KK/qooor+Vev6qK/lXr+qiiv5V6/qooooooor+Vev6qKK/lXr+qiv5V6/qoooor+Veiiiv6qK/lXooor+qiv5V6/qooooor+Vev6qK/lXr+qiiv5V6K/qor+Veiiiiiiv6qKK/lXor+qiv5V6/qor+Vev6qKKKKKK/lXooor+qiv5V6K/qor+Veiv6qK/lXr+qiv5V6/qor+Veiv6qK/lXr+qiv5V6K/qooor+Veiv6qKKK/lXr+qiv5V6K/qor+Veiv6qK/lXr+qiv5V6/qor+Vev6qK/lXoor+qiv5V6/qooooooor+Veiv6qK/lXor+qiiv5V6K/qor+Veiv6qKKK/lXor+qiiiiv5V6KKK/qor+Vev6qKK/lXr+qiv5V6K/qor+Vev6qK/lXor+qiiv5V6KKK/qor+Veiv6qKKKKKKK/lXr+qiv5V6KKKKK/qoooor+Vev6qKKK/lXor+qiiv5V6/qoooor+Vev6qKK/lXoor+qiiv5V6/qooor+Veiiv6qKK/lXr+qiiiv5V6/qoooooooor+Vev6qKK/lXor+qiiiiv5V6KK/qor+Veiiiv6qKK/lXor+qiiiiiiv5V6/qor+Vev6qK/lXooor+qiv5V6/qoor+Vev6qK/lXr+qiv5V6K/qor+Veiv6qKKKKKKKK/lXr+qiv5V6KKK/qor+Vev6qK/lXoor+qiiv5V6KKKK/qoor+Veiv6qKK/lXor+qiv5V6KKKK/qoor+Vev6qK/lXr+qiiv5V6/qoor+Veiiv6qKKKKKKKK/lXor+qiiv5V6K/qoor+Veiv6qK/lXr+qiv5V6K/qoor+Vev6qKKK/lXor+qiv5V6/qor+Veiiv6qK/lXoor+qiiiiv5V6KKKKK/qor+Vev6qK/lXr+qiiiiiiiiiiv5V6K/qor+Veiv6qK/lXr+qiiiiiv5V6/qor+Vev6qKKKK/lXr+qiiv5V6K/qor+Vev6qKKKK/lXr+qiv5V6K/qor+Vev6qK/lXr+qiiv5V6/qoor+Veiv6qKKKKKKKK/lXr+qiv5V6KK/qoooor+Vev6qK/lXr+qiv5V6KKK/qor+Vev6qKK/lXr+qiiv5V6/qoor+Veiv6qKKK/lXr+qiv5V6KKKK/qoor+Vev6qK/lXor+qiv5V6/qoooooooor+Veiv6qK/lXr+qiiv5V6/qooor+Vev6qKKKKK/lXr+qiiv5V6/qor+Vev6qK/lXr+qiv5V6/qor+Vev6qK/lXor+qiv5V6K/qor+Veiv6qKK/lXor+qiv5V6/qor+Veiiv6qKKKKKKKK/lXr+qiv5V6/qor+Veiv6qKKK/lXor+qiiv5V6K/qoooor+Vev6qK/lXr+qiv5V6/qor+Vev6qK/lXr+qiv5V6K/qor+Veiv6qK/lXr+qiv5V6K/qoor+Veiiiiiv6qKKKKKKKKK/lXooooooor+qiv5V6/qor+Vev6qK/lXor+qiv5V6K/qor+Veiiiiiiiv6qK/lXor+qiv5V6K/qoor+Vev6qK/lXr+qiv5V6KKKKK/qooooooooor+Vev6qK/lXr+qiv5V6/qooor+Veiiiiiv6qK/lXr+qiiiv5V6/qoor+Vev6qKKK/lXoor+qiiiv5V6/qooor+Veiiiiv6qKKK/lXoor+qiv5V6/qoooooor+Veiv6qK/lXor+qiv5V6/qor+Vev6qK/lXoor+qiv5V6KK/qoor+Vev6qKK/lXr+qiv5V6/qor+Veiiiiv6qK/lXr+qiv5V6KK/qooor+Vev6qK/lXr+qiv5V6/qor+Veiv6qKKKKKKK/lXor+qiiv5V6/qooor+Vev6qKKK/lXoor+qiiv5V6KK/qor+Veiv6qKKK/lXr+qiv5V6KK/qoor+Vev6qK/lXr+qiiv5V6/qor+Vev6qKKK/lXr+qiiiiiiiiiiv5V6KKKKKKKKK/qor+Vev6qKK/lXoooooor+qiv5V6KKKK/qooor+Veiiv6qKKK/lXr+qiv5V6/qor+Veiiiiiiv6qKKKKKKKKKK/lXor+qiiiiv5V6K/qoooooor+Veiiv6qK/lXor+qiv5V6K/qoor+Vev6qKK/lXoooor+qiv5V6K/qoor+Vev6qK/lXor+qiiv5V6K/qooooooor+Vev6qK/lXr+qiv5V6KK/qooor+Vev6qK/lXr+qiv5V6/qoor+Veiiv6qKK/lXr+qiiiv5V6K/qor+Veiv6qK/lXr+qiiv5V6KK/qoooor+Veiv6qKK/lXoor+qiiiiiiv5V6/qoooooor+Vev6qKK/lXoooor+qiv5V6K/qoor+Vev6qK/lXor+qiiiv5V6/qor+Veiiv6qK/lXr+qiv5V6/qoor+Vev6qK/lXoor+qiv5V6/qor+Veiv6qKKKKKKK/lXr+qiv5V6/qor+Vev6qK/lXoor+qiiv5V6K/qoooor+Vev6qKK/lXr+qiiiiv5V6/qoor+Vev6qK/lXoor+qiiiv5V6/qor+Veiiiv6qK/lXr+qiiv5V6/qoooooooor+Veiiv6qKK/lXr+qiiiiv5V6/qoooooooor+Vev6qKKK/lXor+qiv5V6/qor+Veiv6qK/lXr+qiiv5V6/qoor+Vev6qKKK/lXoor+qiv5V6K/qooooooooor+Veiv6qKK/lXor+qiiiiv5V6/qoooor+Vev6qKK/lXoor+qiiiiv5V6/qoor+Veiiiiiv6qK/lXr+qiiiv5V6/qor+Vev6qKK/lXor+qiiiiiiiiv5V6K/qor+Vev6qK/lXr+qiv5V6/qor+Veiv6qKKK/lXor+qiiv5V6/qooooor+Vev6qKK/lXr+qiiv5V6/qor+Vev6qKK/lXooor+qiiiv5V6/qor+Veiv6qKKKKKKKKK/lXr+qiiiv5V6/qor+Vev6qK/lXoooor+qiiv5V6/qoor+Veiiiiv6qK/lXr+qiiv5V6KKK/qoooor+Vev6qK/lXor+qiv5V6/qooooooooooooooor+Veiv6qK/lXor+qiiv5V6KK/qor+Vev6qKK/lXr+qiiv5V6K/qoor+Vev6qKKK/lXor+qiiv5V6/qor+Veiiv6qK/lXr+qiiiiv5V6K/qor+Vev6qK/lXor+qiiiiiiiiiiiiv5V6K/qor+Vev6qK/lXr+qiv5V6/qor+Vev6qK/lXoor+qiv5V6/qoor+Veiiv6qK/lXr+qiv5V6K/qor+Veiiiiv6qK/lXr+qiiiiiiv5V6K/qoooooooooor+Vev6qKKKK/lXr+qiv5V6/qor+Vev6qKK/lXr+qiiv5V6/qor+Vev6qKKKKK/lXr+qiiv5V6KKKKK/qor+Vev6qK/lXooor+qiv5V6KK/qoor+Vev6qKKKKKKKK/lXr+qiiiv5V6K/qoor+Veiiv6qK/lXor+qiv5V6K/qor+Vev6qKKKK/lXoooor+qiv5V6/qor+Veiv6qK/lXr+qiiv5V6/qoor+Vev6qKKK/lXr+qiiiiiiiiiiv5V6KK/qoooor+Veiiiv6qK/lXr+qiiiiiiv5V6/qoor+Vev6qKKK/lXr+qiiv5V6KK/qooor+Veiiv6qK/lXr+qiv5V6/qor+Vev6qK/lXr+qiiiiiiiiv5V6KK/qooor+Veiv6qK/lXor+qiiv5V6/qor+Vev6qK/lXoooooooooor+qiiiv5V6K/qor+Vev6qK/lXor+qiiv5V6KKKK/qor+Veiiv6qKKKKKKKKKKKKKK/lXr+qiiv5V6K/qor+Vev6qK/lXoor+qiiiv5V6/qooor+Vev6qK/lXor+qiv5V6/qor+Veiv6qK/lXr+qiiv5V6K/qooor+Veiv6qKKKKKKKKK/lXoooooor+qiiv5V6K/qor+Veiiiiiiv6qK/lXoor+qiv5V6/qor+Vev6qK/lXor+qiiiv5V6KK/qoooor+Vev6qK/lXr+qiv5V6KK/qoooooooor+Vev6qKKKKK/lXr+qiiv5V6KK/qor+Vev6qKKKK/lXoor+qiv5V6/qooor+Vev6qKK/lXor+qiv5V6/qooor+Veiiiiv6qKKK/lXr+qiv5V6K/qooooooor+Vev6qK/lXoor+qiv5V6/qor+Vev6qKKK/lXooor+qiiv5V6/qor+Vev6qK/lXooooor+qiv5V6K/qor+Vev6qK/lXr+qiv5V6/qooor+Veiiiiiiv6qKKKKKKKK/lXr+qiv5V6KK/qor+Vev6qKKK/lXor+qiv5V6/qoooor+Vev6qK/lXor+qiiv5V6K/qor+Veiiiiiv6qKK/lXr+qiiv5V6/qooor+Vev6qKK/lXooor+qiiiiiiv5V6/qor+Veiiv6qK/lXr+qiiv5V6/qor+Vev6qK/lXor+qiiiv5V6K/qor+Veiiiiiv6qK/lXr+qiv5V6/qoor+Vev6qKK/lXr+qiv5V6KKK/qor+Vev6qK/lXr+qiiiiiiiiiv5V6/qooooor+Vev6qK/lXr+qiv5V6/qoor+Veiiv6qKK/lXr+qiv5V6/qor+Vev6qK/lXr+qiv5V6K/qoooor+Veiiiiiiiiv6qKK/lXr+qiiv5V6K/qooooooor+Veiiiiiiv6qKKKKKKKK/lXoor+qiiv5V6K/qoor+Vev6qKK/lXr+qiiv5V6KKKK/qor+Vev6qK/lXor+qiiiv5V6KKKKK/qoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooor//Z",
            "authorizeUrl": "https://mp.weixin.qq.com/wxawap/fastregistertpbeta?action=show&create_token=uEfbBwa5QJgZqQZ4_KZSYUkomtiX5cBfWeQNMSgrs6sznFiAGwrAB9365PXVkzCq#wechat_redirect",
            "createToken": "uEfbBwa5QJgZqQZ4_KZSYUkomtiX5cBfWeQNMSgrs6sznFiAGwrAB9365PXVkzCq",
            "headUrl": "https://si.geilicdn.com/wdseller320474174-726900000170a9cad1ca0a21348d_250_250.jpg",
            "leftTime": 258636,
            "name": "萌域之星",
            "requestQrCode": "https://si.geilicdn.com/wxapi-4591000001770520c96b0a2166a4-unadjust_500_500.png",
            "status": 5,
            "statusDesc": "on trial"
            }
        }''')
    # if flow.request.url.find("user.getRegisterInfo") != -1:

        # flow.response.set_text('''{
        #         "status": {
        #             "code": 0,
        #             "message": "OK",
        #             "description": ""
        #         },
        #         "result": {
        #             "companyCode": "91330104MA27WYQ77B",
        #             "companyCodeType": 1,
        #             "companyName": "杭州基育科技有限公司",
        #             "id": 1029,
        #             "mobile": "13148474587",
        #             "reason": "",
        #             "status": 5,
        #             "userName": "钱俊杰",
        #             "wechatId": "qianjunjie-liuxue",
        #             "showNick":true
        #         }
        #     }''')
