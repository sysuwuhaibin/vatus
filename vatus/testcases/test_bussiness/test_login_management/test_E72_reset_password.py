# -*- coding: utf-8 -*-
import time
import unittest
from selenium import webdriver
import settings


class ResetPassword(unittest.TestCase):
    def setUp(self):
        self.driver = None
        self.base_url = settings.test_parameters.get("bussiness_base_url")

    def test_E72_reset_password(self):
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
            # 步骤1：前置条件，登录系统创建用户
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
            driver.find_element_by_id("create_user").click()
            time.sleep(1)
            driver.find_element_by_id("username").clear()
            driver.find_element_by_id("username").send_keys("wuhaibin")
            driver.find_element_by_id("fullname").clear()
            driver.find_element_by_id("fullname").send_keys("wuhaibin")
            driver.find_element_by_id("email").clear()
            driver.find_element_by_id("email").send_keys("wuhaibin@vinzor.com")
            driver.find_element_by_id("password").clear()
            driver.find_element_by_id("password").send_keys("123456")
            driver.find_element_by_id("confirm").clear()
            driver.find_element_by_id("confirm").send_keys("123456")
            time.sleep(3)
            driver.find_element_by_id("confirm_action").click()
            time.sleep(9)
            driver.find_element_by_css_selector("span.user-info").click()
            time.sleep(2)
            driver.find_element_by_link_text(u"退出").click()
            time.sleep(2)
            ###########################################
            # 步骤1：跳转页面，检查邮箱输入格式、长度
            ###########################################
            driver.find_element_by_id("reset_password").click()
            time.sleep(2)
            driver.find_element_by_id("username_email").clear()
            driver.find_element_by_id("submit").click()
            time.sleep(1)
            email_text = driver.find_element_by_id("username_email-error").text
            self.assertEqual("邮箱不能为空", email_text)
            driver.find_element_by_id("username_email").clear()
            driver.find_element_by_id("username_email").\
                send_keys("123456789012345678901234567890123456789012345678901234567890@dsfd.com")
            driver.find_element_by_id("submit").click()
            time.sleep(1)
            email_text = driver.find_element_by_id("username_email-error").text
            self.assertEqual("请输入长度在 1 到 64 之间的字符串", email_text)
            driver.find_element_by_id("username_email").clear()
            driver.find_element_by_id("username_email").send_keys("test@@dfd.com")
            driver.find_element_by_id("submit").click()
            time.sleep(1)
            email_text = driver.find_element_by_id("username_email-error").text
            self.assertEqual("请输入有效的电子邮件地址", email_text)
            ###########################################
            # 步骤2：输入未在系统注册的合法邮箱地址
            ###########################################
            driver.find_element_by_id("username_email").clear()
            driver.find_element_by_id("username_email").send_keys("test@dfd.com")
            driver.find_element_by_id("submit").click()
            time.sleep(3)
            email_text = driver.find_element_by_id("reset_state").text
            self.assertEqual("未注册的用户邮箱地址", email_text)
            ###########################################
            # 步骤3：输入步骤1创建的测试邮件地址
            ###########################################
            driver.find_element_by_id("username_email").clear()
            driver.find_element_by_id("username_email").send_keys("wuhaibin@vinzor.com")
            driver.find_element_by_id("submit").click()
            time.sleep(5)
            login_text = driver.find_element_by_id("login_state").text
            self.assertEqual("邮件已发送，请查收并重设密码", login_text)
            ###########################################
            # 后续步骤： 清理创建的测试数据
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
            driver.find_element_by_css_selector("input.form-control.input-sm").clear()
            driver.find_element_by_css_selector("input.form-control.input-sm").send_keys("wuhaibin")
            time.sleep(5)
            if web_type == 'firefox':
                driver.find_element_by_id("select_all").click()
            elif web_type == 'chrome':
                element = driver.find_element_by_id("select_all")
                webdriver.ActionChains(driver).move_to_element(element).click().perform()
            time.sleep(3)
            driver.find_element_by_id("delete_user").click()
            time.sleep(3)
            driver.find_element_by_id("confirm_delete").click()
            time.sleep(2)
            driver.quit()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
