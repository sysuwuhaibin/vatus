import unittest, time
import testcases.test_bussiness.test_login_management.test_E70_user_login as test_E70_user_login
import testcases.test_bussiness.test_login_management.test_E71_user_modify_password_and_logout as test_E71_user_modify_password_and_logout
import testcases.test_bussiness.test_login_management.test_E72_reset_password as test_E72_reset_password
import testcases.test_bussiness.test_login_management.test_E73_modify_personal_information as test_E73_modify_personal_information
import testcases.test_bussiness.test_user_management.test_E79_create_staff as test_E79_create_staff
import testcases.test_bussiness.test_user_management.test_E81_delete_staff as test_E81_delete_staff
import testcases.test_bussiness.test_user_management.test_E82_reset_staff_password as test_E82_reset_staff_password
import testcases.test_bussiness.test_user_management.test_E83_modify_the_staff_information as test_E83_modify_the_staff_information
import testcases.test_bussiness.test_user_management.test_E112_create_administrator as test_E112_create_administrator
import testcases.test_bussiness.test_user_management.test_E139_delete_administrator as test_E139_delete_administrator
import testcases.test_bussiness.test_user_management.test_E142_disable_enable_administrator as test_E142_disable_enable_administrator


def load_testcase(suites, tc, running_cases_list):
    for running_case in running_cases_list:
        if tc._tests[0]._tests[0]._testMethodName in running_case:
            print("O - %s  " % (tc._tests[0]._tests[0]._testMethodName))
            suites.append(tc)
            return
    print("X - %s  " % (tc._tests[0]._tests[0]._testMethodName))

##############################################
# 转化testlink导出的用例编号格式
##############################################
running_cases_list = []
running_cases = open('running_cases')
for case in running_cases.readlines():
    if case != '\n':
        running_cases_list.append("test_" + case.strip().replace('-', '').replace(':', '_'))
running_cases.close()

##############################################
# 注册待执行的测试用例自动化脚本
##############################################
print("=============================== Start to register TC ==============================")
suites = []
load_testcase(suites, unittest.TestLoader().loadTestsFromModule(test_E70_user_login), running_cases_list)
load_testcase(suites, unittest.TestLoader().loadTestsFromModule(test_E71_user_modify_password_and_logout), running_cases_list)
load_testcase(suites, unittest.TestLoader().loadTestsFromModule(test_E72_reset_password), running_cases_list)
load_testcase(suites, unittest.TestLoader().loadTestsFromModule(test_E73_modify_personal_information), running_cases_list)
load_testcase(suites, unittest.TestLoader().loadTestsFromModule(test_E79_create_staff), running_cases_list)
load_testcase(suites, unittest.TestLoader().loadTestsFromModule(test_E81_delete_staff), running_cases_list)
load_testcase(suites, unittest.TestLoader().loadTestsFromModule(test_E82_reset_staff_password), running_cases_list)
load_testcase(suites, unittest.TestLoader().loadTestsFromModule(test_E83_modify_the_staff_information), running_cases_list)
load_testcase(suites, unittest.TestLoader().loadTestsFromModule(test_E112_create_administrator), running_cases_list)
load_testcase(suites, unittest.TestLoader().loadTestsFromModule(test_E139_delete_administrator), running_cases_list)
load_testcase(suites, unittest.TestLoader().loadTestsFromModule(test_E142_disable_enable_administrator), running_cases_list)

print("============================ VinzorBE Auto Test Report ============================")
print("Total Selected Testcases: %d" % len(suites))
time.sleep(2)

test_suites = unittest.TestSuite(suites)
unittest.TextTestRunner(verbosity=2).run(test_suites)

