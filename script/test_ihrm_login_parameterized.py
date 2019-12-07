import unittest
import logging
from utils import assert_common, read_login_data
from parameterized import parameterized
from api.login_api import LoginApi


class TestIHRMLoginParameterized(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.login_api = LoginApi()


    @parameterized.expand(read_login_data)
    def test01_login_success(self,mobile,password,http_code,success,code,message):
        response = self.login_api.login(mobile,password)
        logging.info("登陆接口返回数据为:{}".format(response.json()))
        # 断言
        assert_common(self,response,http_code,success,code,message)
