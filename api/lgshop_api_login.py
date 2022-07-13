import requests


class LgShopLogin:

    def __init__(self):
        self.url_verify = "http://localhost/index.php?m=Home&c=User&a=verify"
        self.url_login = "http://localhost/index.php?m=Home&c=User&a=do_login"

    # 封装获取验证码接口
    def get_verify(self):
        response = requests.get(url=self.url_verify)
        return response

    # 封装登录接口
    def login(self, data, headers):
        return requests.post(url=self.url_login, data=data, headers=headers)

    def get_verify_session(self, session):
        return session.get(url= self.url_verify)

    def login_session(self, session, data, headers):
        return session.post(url=self.url_login, data=data, headers=headers)


if __name__ == '__main__':
    lg_api = LgShopLogin()
    response = lg_api.get_verify()
    print(response.content)
    print(response.cookies)
    a = str(response.cookies)
    print(a[27:63])
    data = "username=13800138006&password=123456&verify_code=8888"
    headers = {"Content-Type": "application/x-www-form-urlencoded",
               "Cookie": a[27:63]}
    response = lg_api.login(data, headers)
    print(response.json())
