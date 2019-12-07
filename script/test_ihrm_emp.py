import unittest

import pymysql

import app,logging
from api.login_api import LoginApi
from requests import Response
from utils import assert_common,DBUtiles
from api.emp_api import EmpApi


class TestEmp(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        cls.emp_api = EmpApi()

        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test01_add_emp(self):
        response = self.emp_api.add_emp("花花07","138999999997")
        logging.info("添加员工接口返回数据为:{}".format(response.json()))
        # 断言
        assert_common(self,response,200,True,10000,"操作成功")


        #获取添加员工接口返回的json数据
        jsonData = response.json()
        # 获取员工id
        emp_id = jsonData.get('data').get('id')
        # 保存员工id到全局变量
        #这里需要仙剑一个员工id到APP中
        app.EMPID = emp_id
        # 打印查看有没有保存成功
        logging.info("保存的员工ID:{}".format(app.EMPID))


    def test02_query_emp(self):
        #调用查询员工接口
        response = self.emp_api.query_emp()
        #打印
        logging.info("查询员工接口返回的数据为:{}".format(response.json()))
        # 断言响应数据
        assert_common(self,response,200,True,10000,"操作成功")

    def test03_modify_emp(self):
        #调用修改员工接口
        response = self.emp_api.modify_emp("奥特曼")
        # 打印
        logging.info("修改员工接口返回的数据为:{}",format(response.json()))
        #断言响应数据
        assert_common(self, response, 200, True, 10000, "操作成功")

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

        self.assertEqual("奥特曼",result)




    def test04_delete_emp(self):
        response = self.emp_api.delete_emp()

        logging.info("删除员工接口返回的数据为:{}",format(response.json()))
