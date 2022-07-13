import requests
import unittest

from api.lgshop_api_regist import LgShopRegist


class TestRegister(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.reg = LgShopRegist()

    def setUp(self) -> None:
        self.session = requests.Session()
        
    def test001(self):
        response = self.reg.get_verify_session(self.session)
        print(response.cookies)
        data = "auth_code=TPSHOP&scene=1&username=13800000002&verify_code=8888&password=519475228fe35ad067744465c42a19b2" \
               "&password2=519475228fe35ad067744465c42a19b2 "
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        response = self.reg.register_session(self.session, data, headers)
        print(response.json())

    def test002(self):
        response = self.reg.get_verify_session(self.session)
        print(response.cookies)
        # 两次输入密码不一致
        data = "auth_code=TPSHOP&scene=1&username=13800000002&verify_code=8888&password=519475228fe35ad067744465c42a19b2" \
               "&password2=519475228fe35ad067744465cb2 "
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        response = self.reg.register_session(self.session, data, headers)
        print(response.json())