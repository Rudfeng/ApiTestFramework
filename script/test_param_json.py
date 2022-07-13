from parameterized import parameterized
import requests
import unittest
from utils import read_json_data
from api.lgshop_api_login import LgShopLogin


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.login = LgShopLogin()
        self.session = requests.Session()

    def tearDown(self) -> None:
        self.session.close()

    @parameterized.expand(read_json_data("../data/login_data.json"))
    def test001(self, case_name, username, password, verify_code, msg, status):
        response = self.login.get_verify_session(self.session)
        print(response.cookies)
        data = f"username={username}&password={password}&verify_code={verify_code}"
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        response = self.login.login_session(self.session, data, headers)
        print(f"{case_name}", response.json())
        self.assertEqual(status, response.json().get("status"))
        self.assertEqual(msg, response.json().get("msg"))
