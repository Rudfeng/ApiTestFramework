import unittest, requests
from api.lgshop_api_login import LgShopLogin


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.login = LgShopLogin()
        self.session = requests.Session()

    def test001(self):
        response = self.login.get_verify_session(self.session)
        print(response.cookies)
        data = "username=13800138006&password=123456&verify_code=8888"
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        response = self.login.login_session(self.session, data, headers)
        print(response.json())
        self.assertEqual(1, response.json().get("status"))
        self.assertEqual('登陆成功', response.json().get("msg"))

    def test002(self):
        response = self.login.get_verify_session(self.session)
        print(response.cookies)
        data = "username=13800138006&password=qewafat&verify_code=8888"
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        response = self.login.login_session(self.session, data, headers)
        print(response.json())
        self.assertEqual(-2, response.json().get("status"))
        self.assertEqual('密码错误!', response.json().get("msg"))
        self.assertEqual(200, response.status_code)

    def test003(self):
        response = self.login.get_verify_session(self.session)
        print(response.cookies)
        data = "username=13800138006&password=123456&verify_code=fase"
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        response = self.login.login_session(self.session, data, headers)
        print(response.json())
        self.assertEqual(0, response.json().get("status"))
        self.assertEqual('验证码错误', response.json().get("msg"))
        self.assertEqual(200, response.status_code)

    def test004(self):
        response = self.login.get_verify_session(self.session)
        print(response.cookies)
        data = "username=12356236&password=123456&verify_code=8888"
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        response = self.login.login_session(self.session, data, headers)
        print(response.json())
        self.assertEqual(-1, response.json().get("status"))
        self.assertEqual('账号不存在!', response.json().get("msg"))
        self.assertEqual(200, response.status_code)
