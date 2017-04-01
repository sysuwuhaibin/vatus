# -*- coding: utf-8 -*-
import time
import unittest
from selenium import webdriver
import settings


class Modifypasswd(unittest.TestCase):
    def setUp(self):
        self.driver = None
        self.base_url = settings.test_parameters.get("bussiness_base_url")

    def test_E71_user_modify_password_and_logout(self):
        web_types = settings.test_parameters.get("web_types")
        for web_type in web_types:
            if web_type == 'firefox':
                self.driver = webdriver.Firefox()
            elif web_type == 'chrome':
                self.driver = webdriver.Chrome()

            self.driver.implicitly_wait(30)
            driver = self.driver
            driver.get(self.base_url)
            driver.maximize_window()

            ###########################################
            # 前置条件：登录系统
            ###########################################
            driver.find_element_by_id("input_username").clear()
            driver.find_element_by_id("input_username").send_keys("admin")
            driver.find_element_by_id("input_password").clear()
            driver.find_element_by_id("input_password").send_keys("admin123")
            driver.find_element_by_id("login_btn").click()
            time.sleep(5)
            driver.find_element_by_css_selector("span.user-info").click()
            driver.find_element_by_link_text(u"个人信息").click()
            ###########################################
            # 步骤1：原密码错误
            ###########################################
            time.sleep(2)
            driver.find_element_by_id("reset-passwd").click()
            time.sleep(2)
            driver.find_element_by_id("oldpasswd").clear()
            driver.find_element_by_id("oldpasswd").send_keys("admin")
            driver.find_element_by_id("newpasswd").clear()
            driver.find_element_by_id("newpasswd").send_keys("admin122")
            driver.find_element_by_id("confirmpasswd").clear()
            driver.find_element_by_id("confirmpasswd").send_keys("admin122")
            driver.find_element_by_id("confirm_resetpasswd").click()
            time.sleep(11)
            ###########################################
            # 步骤2：输入的旧密码长度小于6个字符或者大于25个字符
            ###########################################
            driver.find_element_by_id("reset-passwd").click()
            time.sleep(2)
            driver.find_element_by_id("oldpasswd").clear()
            driver.find_element_by_id("oldpasswd").send_keys("1234")
            driver.find_element_by_id("newpasswd").clear()
            driver.find_element_by_id("newpasswd").send_keys("admin122")
            driver.find_element_by_id("confirmpasswd").clear()
            driver.find_element_by_id("confirmpasswd").send_keys("admin122")
            driver.find_element_by_id("confirm_resetpasswd").click()
            time.sleep(1)
            self.assertEqual("长度不少于5个字", driver.find_element_by_id("oldpasswd-error").text)
            driver.find_element_by_id("oldpasswd").clear()
            driver.find_element_by_id("oldpasswd").send_keys("12345678901234567890123456789012345678901234567890123456789012345")
            driver.find_element_by_id("newpasswd").clear()
            driver.find_element_by_id("newpasswd").send_keys("admin122")
            driver.find_element_by_id("confirmpasswd").clear()
            driver.find_element_by_id("confirmpasswd").send_keys("admin122")
            driver.find_element_by_id("confirm_resetpasswd").click()
            time.sleep(1)
            self.assertEqual("长度不超过64个字", driver.find_element_by_id("oldpasswd-error").text)
            ###########################################
            # 步骤3：密码长度小于5个字符和超过64个字符
            ###########################################
            driver.find_element_by_id("oldpasswd").clear()
            driver.find_element_by_id("oldpasswd").send_keys("admin123")
            driver.find_element_by_id("newpasswd").clear()
            driver.find_element_by_id("newpasswd").send_keys("1234")
            driver.find_element_by_id("confirmpasswd").clear()
            driver.find_element_by_id("confirmpasswd").send_keys("1234")
            driver.find_element_by_id("confirm_resetpasswd").click()
            time.sleep(1)
            self.assertEqual("长度不少于5个字", driver.find_element_by_id("newpasswd-error").text)
            self.assertEqual("长度不少于5个字", driver.find_element_by_id("confirmpasswd-error").text)
            driver.find_element_by_id("newpasswd").clear()
            driver.find_element_by_id("newpasswd").send_keys("12345678901234567890123456789012345678901234567890123456789012345")
            driver.find_element_by_id("confirmpasswd").clear()
            driver.find_element_by_id("confirmpasswd").send_keys("12345678901234567890123456789012345678901234567890123456789012345")
            driver.find_element_by_id("confirm_resetpasswd").click()
            time.sleep(1)
            self.assertEqual("长度不超过64个字", driver.find_element_by_id("newpasswd-error").text)
            self.assertEqual("长度不超过64个字", driver.find_element_by_id("confirmpasswd-error").text)
            ###########################################
            # 步骤4：新密码不一致
            ###########################################
            driver.find_element_by_id("oldpasswd").clear()
            driver.find_element_by_id("oldpasswd").send_keys("admin123")
            driver.find_element_by_id("newpasswd").clear()
            driver.find_element_by_id("newpasswd").send_keys("1234567890")
            driver.find_element_by_id("confirmpasswd").clear()
            driver.find_element_by_id("confirmpasswd").send_keys("1234567")
            driver.find_element_by_id("confirm_resetpasswd").click()
            time.sleep(1)
            self.assertEqual("确认密码不一致", driver.find_element_by_id("confirmpasswd-error").text)
            ###########################################
            # 步骤5：输入正确新旧密码,重新登录
            ###########################################
            driver.find_element_by_id("oldpasswd").clear()
            driver.find_element_by_id("oldpasswd").send_keys("admin123")
            driver.find_element_by_id("newpasswd").clear()
            driver.find_element_by_id("newpasswd").send_keys("123456")
            driver.find_element_by_id("confirmpasswd").clear()
            driver.find_element_by_id("confirmpasswd").send_keys("123456")
            driver.find_element_by_id("confirm_resetpasswd").click()
            time.sleep(1)
            # 退出
            time.sleep(8)
            driver.find_element_by_css_selector("span.user-info").click()
            time.sleep(1)
            driver.find_element_by_link_text(u"退出").click()
            time.sleep(3)
            driver.find_element_by_id("input_username").clear()
            driver.find_element_by_id("input_username").send_keys("admin")
            driver.find_element_by_id("input_password").clear()
            driver.find_element_by_id("input_password").send_keys("123456")
            driver.find_element_by_id("login_btn").click()
            ###########################################
            # 后置条件: 恢复密码,有助多次测试
            ###########################################
            time.sleep(5)
            driver.find_element_by_css_selector("span.user-info").click()
            driver.find_element_by_link_text(u"个人信息").click()
            time.sleep(2)
            driver.find_element_by_id("reset-passwd").click()
            time.sleep(2)
            driver.find_element_by_id("oldpasswd").clear()
            driver.find_element_by_id("oldpasswd").send_keys("123456")
            driver.find_element_by_id("newpasswd").clear()
            driver.find_element_by_id("newpasswd").send_keys("admin123")
            driver.find_element_by_id("confirmpasswd").clear()
            driver.find_element_by_id("confirmpasswd").send_keys("admin123")
            driver.find_element_by_id("confirm_resetpasswd").click()
            time.sleep(2)
            driver.quit()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
