import unittest
from parameterized import parameterized
import app,logging
from utils import assert_common,DBUtiles,resd_add_emp_data,resd_query_emp_data,read_modify_emp_data,read_delete_emp_data
from api.emp_api import EmpApi

class TestEmpParameterized(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.emp_api = EmpApi()
    @parameterized.expand(resd_add_emp_data)
    def test01_add_emp(self,username,mobile,http_code,success,code,message):
        response = self.emp_api.add_emp(username,mobile)
        logging.info("添加员工接口返回数据为:{}".format(response.json()))
        # 断言
        assert_common(self,response,http_code,success,code,message)

        #获取添加员工接口返回的json数据
        jsonData = response.json()
        # 获取员工id
        emp_id = jsonData.get('data').get('id')
        # 保存员工id到全局变量
        #这里需要仙剑一个员工id到APP中
        app.EMPID = emp_id
        # 打印查看有没有保存成功
        logging.info("保存的员工ID:{}".format(app.EMPID))

    @parameterized.expand(resd_query_emp_data)
    def test02_query_emp(self,http_code,success,code,message):
        #调用查询员工接口
        response = self.emp_api.query_emp()
        #打印
        logging.info("查询员工接口返回的数据为:{}".format(response.json()))
        # 断言响应数据
        assert_common(self,response,http_code,success,code,message)

    @parameterized.expand(read_modify_emp_data)
    def test03_modify_emp(self,username,http_code,success,code,message):
        #调用修改员工接口
        response = self.emp_api.modify_emp(username)
        # 打印
        logging.info("修改员工接口返回的数据为:{}",format(response.json()))
        #断言响应数据
        assert_common(self, response, http_code, success, code, message)

        # # 断言数据库总的数据
        # conn = pymysql.connect("182.92.81.159","readuser",'iHRM_user_2019','ihrm')
        # # 获取游标
        # cursor = conn.cursor()
        # # 执行查询语句
        # query_sql = "select username from bs_user where id={} limit 1".format(app.EMPID)
        # cursor.execute(query_sql)
        # result = cursor.fetchone()
        # cursor.close()
        # conn.close()

        with DBUtiles("182.92.81.159","readuser",'iHRM_user_2019','ihrm') as db:
            query_sql = "select username from bs_user where id={} limit 1".format(app.EMPID)
            db.execute(query_sql)
            result = db.fetchone()

        logging.info("--------查询数据库中员工ID为{}的username是:{}".format(app.EMPID,result[0]))

        self.assertEqual(username,result)



    @parameterized.expand(read_delete_emp_data())
    def test04_delete_emp(self,http_code,success,code,message):
        response = self.emp_api.delete_emp()

        logging.info("删除员工接口返回的数据为:{}",format(response.json()))
        assert_common(self,response,http_code,success,code,message)
