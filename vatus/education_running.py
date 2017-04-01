import unittest, time
import testcases.test_education.test_login_management.test_E70_user_login as test_E70_user_login
import testcases.test_education.test_login_management.test_E71_user_modify_password_and_logout as test_E71_user_modify_password_and_logout
import testcases.test_education.test_login_management.test_E72_reset_password as test_E72_reset_password
import testcases.test_education.test_login_management.test_E73_modify_personal_information as test_E73_modify_personal_information
import testcases.test_education.test_user_management.test_E79_create_student as test_E79_create_student
import testcases.test_education.test_user_management.test_E81_delete_student as test_E81_delete_student
import testcases.test_education.test_user_management.test_E82_reset_student_password as test_E82_reset_student_password
import testcases.test_education.test_user_management.test_E83_modify_the_students_information as test_E83_modify_the_students_information
import testcases.test_education.test_user_management.test_E85_create_teacher as test_E85_create_teacher
import testcases.test_education.test_user_management.test_E87_delete_teacher as test_E87_delete_teacher
import testcases.test_education.test_user_management.test_E88_modify_the_teachers_information as test_E88_modify_the_teachers_information
import testcases.test_education.test_user_management.test_E89_disable_enable_teacher as test_E89_disable_enable_teacher
import testcases.test_education.test_user_management.test_E112_create_administrator as test_E112_create_administrator
import testcases.test_education.test_user_management.test_E139_delete_administrator as test_E139_delete_administrator
import testcases.test_education.test_user_management.test_E142_disable_enable_administrator as test_E142_disable_enable_administrator


def load_testcase(suites, tc, running_cases_list):
    for running_case in running_cases_list:
        if tc._tests[0]._tests[0]._testMethodName in running_case:
            suites.append(tc)
            break

##############################################
# 转化testlink导出的用例编号格式
##############################################
running_cases_list = []
running_cases = open('running_cases')
for case in running_cases.readlines():
    if case != '\n':
        running_cases_list.append("test_" + case.strip().replace('-', '').replace(':', '_'))
running_cases.close()
suites = []

##############################################
# 注册待执行的测试用例自动化脚本
##############################################
load_testcase(suites, unittest.TestLoader().loadTestsFromModule(test_E70_user_login), running_cases_list)
load_testcase(suites, unittest.TestLoader().loadTestsFromModule(test_E71_user_modify_password_and_logout), running_cases_list)
load_testcase(suites, unittest.TestLoader().loadTestsFromModule(test_E72_reset_password), running_cases_list)
load_testcase(suites, unittest.TestLoader().loadTestsFromModule(test_E73_modify_personal_information), running_cases_list)
load_testcase(suites, unittest.TestLoader().loadTestsFromModule(test_E79_create_student), running_cases_list)
load_testcase(suites, unittest.TestLoader().loadTestsFromModule(test_E81_delete_student), running_cases_list)
load_testcase(suites, unittest.TestLoader().loadTestsFromModule(test_E82_reset_student_password), running_cases_list)
load_testcase(suites, unittest.TestLoader().loadTestsFromModule(test_E83_modify_the_students_information), running_cases_list)
load_testcase(suites, unittest.TestLoader().loadTestsFromModule(test_E85_create_teacher), running_cases_list)
load_testcase(suites, unittest.TestLoader().loadTestsFromModule(test_E87_delete_teacher), running_cases_list)
load_testcase(suites, unittest.TestLoader().loadTestsFromModule(test_E88_modify_the_teachers_information), running_cases_list)
load_testcase(suites, unittest.TestLoader().loadTestsFromModule(test_E89_disable_enable_teacher), running_cases_list)
load_testcase(suites, unittest.TestLoader().loadTestsFromModule(test_E112_create_administrator), running_cases_list)
load_testcase(suites, unittest.TestLoader().loadTestsFromModule(test_E139_delete_administrator), running_cases_list)
load_testcase(suites, unittest.TestLoader().loadTestsFromModule(test_E142_disable_enable_administrator), running_cases_list)

print("======================= VinzorEE Auto Test Report =======================")
print("Total Testcases: %d" % len(suites))
time.sleep(2)

test_suites = unittest.TestSuite(suites)
unittest.TextTestRunner(verbosity=2).run(test_suites)