# 导包
import unittest,app
import time
from script.test_ihem_login import TestIHRMLogin
from tools.HTMLTestRunner import HTMLTestRunner
# from script.test_ihrm_emp import TestEmp
from script.test_ihrm_emp_parameterized import TestEmpParameterized

# 实例化测试套件
suite = unittest.TestSuite()

#添加测试用例
suite.addTest(unittest.makeSuite(TestIHRMLogin))
suite.addTest(unittest.makeSuite(TestEmpParameterized))

# 设置测试报告路径个名称
report_path = app.BASE_DIR + "/report/ihrm{}.html".format(time.strftime('%Y%m%d%H%M%S'))
# 打开文件
with open(report_path,mode='wb') as f:
    # 实例化HTMLTestRuner
    runner = HTMLTestRunner(f,verbosity=1,title="IHRM人力资源管理系统登录接口测试报告",
                            description="测试登录接口和员工管理模块")

# 使用runner运行测试套件生成测试报告
    runner.run(suite)


