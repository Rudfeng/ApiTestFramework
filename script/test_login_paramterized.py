from parameterized import parameterized
import requests
import unittest

from api.lgshop_api_login import LgShopLogin


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.login = LgShopLogin()
        self.session = requests.Session()

    @parameterized.expand([('13800138006', '123456', '8888', '登陆成功', 1),
                           ('13800138006', '1234567', '8888', '密码错误!', -2),
                           ('13800138006', '123456', '3262', '验证码错误', 0),
                           ('13815351306', '123456', '8888', '账号不存在!', -1)])
    def test001(self, username, password, verify_code, msg, status):
        response = self.login.get_verify_session(self.session)
        print(response.cookies)
        data = f"username={username}&password={password}&verify_code={verify_code}"
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        response = self.login.login_session(self.session, data, headers)
        print(response.json())
        self.assertEqual(status, response.json().get("status"))
        self.assertEqual(msg, response.json().get("msg"))
