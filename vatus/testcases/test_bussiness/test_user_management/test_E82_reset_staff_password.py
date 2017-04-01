# -*- coding: utf-8 -*-
import time
import unittest
from selenium import webdriver
import settings


class ResetStaffPassword(unittest.TestCase):
    def setUp(self):
        self.driver = None
        self.base_url = settings.test_parameters.get("bussiness_base_url")

    def test_E82_reset_staff_password(self):
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
            driver.find_element_by_link_text(u"用户管理").click()
            time.sleep(1)
            driver.find_element_by_link_text(u"员工").click()
            time.sleep(3)
            ###########################################
            # 步骤1：不选任何员工，点击重置，检查提示
            ###########################################
            driver.find_element_by_id("modify_password").click()
            time.sleep(2)
            self.assertEqual("请选择一个或多个要重置密码的用户", driver.find_element_by_class_name("gritter-without-image").
                             find_element_by_tag_name("p").text)
            time.sleep(8)
            ###########################################
            # 步骤2：重置密码输入为空
            ###########################################
            if web_type == 'firefox':
                driver.find_element_by_id("select_all").click()
            elif web_type == 'chrome':
                element = driver.find_element_by_id("select_all")
                webdriver.ActionChains(driver).move_to_element(element).click().perform()
            time.sleep(3)
            driver.find_element_by_id("modify_password").click()
            time.sleep(2)
            driver.find_element_by_id("confirm_action").click()
            self.assertEqual("请输入用户密码", driver.find_element_by_id("password-error").text)
            self.assertEqual("请输入用户密码", driver.find_element_by_id("confirm-error").text)
            ###########################################
            # 步骤3：重置密码输入长度不符合要求
            ###########################################
            driver.find_element_by_id("password").clear()
            driver.find_element_by_id("password").send_keys("1234")
            driver.find_element_by_id("confirm").clear()
            driver.find_element_by_id("confirm").send_keys("1234")
            driver.find_element_by_id("confirm_action").click()
            time.sleep(1)
            self.assertEqual("长度5-64个字", driver.find_element_by_id("password-error").text)
            self.assertEqual("长度5-64个字", driver.find_element_by_id("confirm-error").text)
            driver.find_element_by_id("password").clear()
            driver.find_element_by_id("password").send_keys("1234567890123456789012345678901"
                                                            "234567890123456789012345678901234567890")
            driver.find_element_by_id("confirm").clear()
            driver.find_element_by_id("confirm").send_keys("123456789012345678901234567890123"
                                                           "4567890123456789012345678901234567890")
            driver.find_element_by_id("confirm_action").click()
            time.sleep(1)
            self.assertEqual("长度5-64个字", driver.find_element_by_id("password-error").text)
            self.assertEqual("长度5-64个字", driver.find_element_by_id("confirm-error").text)
            ###########################################
            # 步骤4：重置密码两次输入不一致
            ###########################################
            driver.find_element_by_id("password").clear()
            driver.find_element_by_id("password").send_keys("87654321")
            driver.find_element_by_id("confirm").clear()
            driver.find_element_by_id("confirm").send_keys("987654321")
            driver.find_element_by_id("confirm_action").click()
            time.sleep(1)
            self.assertEqual("确认密码不一致", driver.find_element_by_id("confirm-error").text)
            ###########################################
            # 步骤4：重置密码成功验证登录
            ###########################################
            driver.find_element_by_id("password").clear()
            driver.find_element_by_id("password").send_keys("987654321")
            driver.find_element_by_id("confirm").clear()
            driver.find_element_by_id("confirm").send_keys("987654321")
            driver.find_element_by_id("confirm_action").click()
            time.sleep(8)
            driver.find_element_by_css_selector("span.user-info").click()
            time.sleep(1)
            driver.find_element_by_link_text(u"退出").click()
            time.sleep(2)
            driver.find_element_by_id("input_username").clear()
            driver.find_element_by_id("input_username").send_keys("staff")
            driver.find_element_by_id("input_password").clear()
            driver.find_element_by_id("input_password").send_keys("987654321")
            driver.find_element_by_id("login_btn").click()
            time.sleep(3)
            driver.find_element_by_css_selector("span.user-info").click()
            time.sleep(1)
            driver.find_element_by_link_text(u"退出").click()
            time.sleep(2)
            ###########################################
            # 后置条件: 恢复重置为初始密码
            ###########################################
            driver.find_element_by_id("input_username").clear()
            driver.find_element_by_id("input_username").send_keys("admin")
            driver.find_element_by_id("input_password").clear()
            driver.find_element_by_id("input_password").send_keys("admin123")
            driver.find_element_by_id("login_btn").click()
            time.sleep(5)
            driver.find_element_by_link_text(u"用户管理").click()
            time.sleep(1)
            driver.find_element_by_link_text(u"员工").click()
            time.sleep(3)
            if web_type == 'firefox':
                driver.find_element_by_id("select_all").click()
            elif web_type == 'chrome':
                element = driver.find_element_by_id("select_all")
                webdriver.ActionChains(driver).move_to_element(element).click().perform()
            time.sleep(3)
            driver.find_element_by_id("modify_password").click()
            time.sleep(2)
            driver.find_element_by_id("password").clear()
            driver.find_element_by_id("password").send_keys("admin123")
            driver.find_element_by_id("confirm").clear()
            driver.find_element_by_id("confirm").send_keys("admin123")
            driver.find_element_by_id("confirm_action").click()
            time.sleep(3)
            driver.quit()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
