import requests


class LgShopRegist:

    def __init__(self):
        self.url_verify = "http://localhost/index.php?m=Home&c=User&a=verify&type=user_reg"
        self.url_register = "http://localhost/index.php/Home/User/reg.html"

    def get_verify(self):
        return requests.get(self.url_verify)

    def register(self, data, headers):
        return requests.post(url=self.url_register, data=data, headers=headers)

    # 使用seesion封装接口
    def get_verify_session(self, session):
        return session.get(url=self.url_verify)

    def register_session(self, session, data, headers):
        return session.post(url=self.url_register,
                            data=data,
                            headers=headers)


if __name__ == '__main__':
    # lg_register = LgShopRegist()
    # response = lg_register.get_verify()
    # print(response.content)
    # print(response.cookies)
    # # 发现cookies返回的session长度固定，用列表切片做自动化
    # a = str(response.cookies)
    # print(a[27:63])
    # headers = {"Content-Type": "application/x-www-form-urlencoded",
    #            "Cookie": a[27:63]}
    #
    # data = "auth_code=TPSHOP&scene=1&username=13800000002&verify_code=8888&password=519475228fe35ad067744465c42a19b2" \
    #        "&password2=519475228fe35ad067744465c42a19b2 "
    # response = lg_register.register(data, headers)
    # print(response.json())

    session = requests.Session()
    reg = LgShopRegist()
    response = reg.get_verify_session(session)
    print(response.content)
    
    data = "auth_code=TPSHOP&scene=1&username=13800000002&verify_code=8888&password=519475228fe35ad067744465c42a19b2" \
           "&password2=519475228fe35ad067744465c42a19b2 "
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    response = reg.register_session(session, data, headers)
    print(response.json())