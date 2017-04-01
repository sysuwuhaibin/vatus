# -*- coding: utf-8 -*-
import time
import unittest

from selenium import webdriver

import settings


class CreateAdministrator(unittest.TestCase):
    def setUp(self):
        self.driver = None
        self.base_url = settings.test_parameters.get("education_base_url")

    def test_E112_create_administrator(self):
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
            driver.find_element_by_id("input_username").send_keys(settings.test_parameters.get("admin_username"))
            driver.find_element_by_id("input_password").clear()
            driver.find_element_by_id("input_password").send_keys(settings.test_parameters.get("admin_password"))
            driver.find_element_by_id("login_btn").click()
            time.sleep(5)
            ###########################################
            # 步骤1：全部输入为空，检查提示
            ###########################################
            driver.find_element_by_link_text(u"用户管理").click()
            time.sleep(1)
            driver.find_element_by_link_text(u"管理员").click()
            time.sleep(3)
            driver.find_element_by_id("create_user").click()
            time.sleep(1)
            driver.find_element_by_id("confirm_action").click()
            time.sleep(1)
            self.assertEqual("请输入用户名", driver.find_element_by_id("username-error").text)
            self.assertEqual("请输入姓名", driver.find_element_by_id("fullname-error").text)
            self.assertEqual("请输入邮件地址", driver.find_element_by_id("email-error").text)
            self.assertEqual("请输入用户密码", driver.find_element_by_id("password-error").text)
            self.assertEqual("请输入用户密码", driver.find_element_by_id("confirm-error").text)
            ###########################################
            # 步骤3：长度输入不符合,密码不一致，检查提示
            ###########################################
            driver.find_element_by_id("username").clear()
            driver.find_element_by_id("username").\
                send_keys("1234567890123456789012345678901234567890123456789012345678901234567890")
            time.sleep(1)
            self.assertEqual("长度不超过64个字", driver.find_element_by_id("username-error").text)
            driver.find_element_by_id("fullname").clear()
            driver.find_element_by_id("fullname").\
                send_keys("1234567890123456789012345678901234567890123456789012345678901234567890")
            time.sleep(1)
            self.assertEqual("长度不超过64个字", driver.find_element_by_id("fullname-error").text)
            driver.find_element_by_id("email").clear()
            driver.find_element_by_id("email").\
                send_keys("123456789012345678901234567890123456789012345678901234567890@dsfd.com")
            time.sleep(1)
            self.assertEqual("长度1-64个字", driver.find_element_by_id("email-error").text)
            driver.find_element_by_id("password").clear()
            driver.find_element_by_id("password").send_keys("1234")
            time.sleep(1)
            self.assertEqual("长度5-64个字", driver.find_element_by_id("password-error").text)
            driver.find_element_by_id("confirm").clear()
            driver.find_element_by_id("confirm").send_keys("1234")
            time.sleep(1)
            self.assertEqual("长度5-64个字", driver.find_element_by_id("confirm-error").text)
            driver.find_element_by_id("password").clear()
            driver.find_element_by_id("password").\
                send_keys("1234567890123456789012345678901234567890123456789012345678901234567890")
            time.sleep(1)
            self.assertEqual("长度5-64个字", driver.find_element_by_id("password-error").text)
            driver.find_element_by_id("confirm").clear()
            driver.find_element_by_id("confirm").\
                send_keys("1234567890123456789012345678901234567890123456789012345678901234567890")
            time.sleep(1)
            self.assertEqual("长度5-64个字", driver.find_element_by_id("confirm-error").text)
            driver.find_element_by_id("password").clear()
            driver.find_element_by_id("password").send_keys("12345")
            driver.find_element_by_id("confirm").clear()
            driver.find_element_by_id("confirm").send_keys("123456")
            time.sleep(3)
            self.assertEqual("确认密码不一致", driver.find_element_by_id("confirm-error").text)
            ###########################################
            # 步骤4：正常输入
            ###########################################
            driver.find_element_by_id("username").clear()
            driver.find_element_by_id("username").send_keys("createadmin")
            driver.find_element_by_id("fullname").clear()
            driver.find_element_by_id("fullname").send_keys("createadmin")
            driver.find_element_by_id("email").clear()
            driver.find_element_by_id("email").send_keys("createadmin@vinzor.com")
            driver.find_element_by_id("password").clear()
            driver.find_element_by_id("password").send_keys("123456")
            driver.find_element_by_id("confirm").clear()
            driver.find_element_by_id("confirm").send_keys("123456")
            time.sleep(3)
            driver.find_element_by_id("confirm_action").click()
            time.sleep(5)
            self.assertEqual("用户 createadmin 创建成功", driver.find_element_by_class_name("gritter-without-image").
                             find_element_by_tag_name("p").text)
            ###########################################
            # 步骤5：正常输入但ID已存在，检查提示信息
            ###########################################
            driver.find_element_by_id("create_user").click()
            time.sleep(1)
            driver.find_element_by_id("username").clear()
            driver.find_element_by_id("username").send_keys("createadmin")
            driver.find_element_by_id("fullname").clear()
            driver.find_element_by_id("fullname").send_keys("createadmin")
            driver.find_element_by_id("email").clear()
            driver.find_element_by_id("email").send_keys("admin02@vinzor.com")
            driver.find_element_by_id("password").clear()
            driver.find_element_by_id("password").send_keys("123456")
            driver.find_element_by_id("confirm").clear()
            driver.find_element_by_id("confirm").send_keys("123456")
            time.sleep(3)
            driver.find_element_by_id("confirm_action").click()
            time.sleep(2)
            self.assertEqual("用户名已经存在", driver.find_element_by_id("username-error").text)
            ###########################################
            # 步骤5：正常输入但邮箱已存在，检查提示信息
            ###########################################
            driver.find_element_by_class_name("close").click()
            time.sleep(1)
            driver.find_element_by_id("create_user").click()
            time.sleep(1)
            driver.find_element_by_id("username").clear()
            driver.find_element_by_id("username").send_keys("admin02")
            driver.find_element_by_id("fullname").clear()
            driver.find_element_by_id("fullname").send_keys("admin02")
            driver.find_element_by_id("email").clear()
            driver.find_element_by_id("email").send_keys("createadmin@vinzor.com")
            driver.find_element_by_id("password").clear()
            driver.find_element_by_id("password").send_keys("123456")
            driver.find_element_by_id("confirm").clear()
            driver.find_element_by_id("confirm").send_keys("123456")
            time.sleep(3)
            driver.find_element_by_id("confirm_action").click()
            time.sleep(2)
            self.assertEqual("邮件地址已被使用", driver.find_element_by_id("email-error").text)
            time.sleep(1)
            driver.find_element_by_class_name("close").click()
            time.sleep(1)
            driver.find_element_by_css_selector("span.user-info").click()
            time.sleep(1)
            driver.find_element_by_link_text(u"退出").click()
            time.sleep(2)
            driver.find_element_by_id("input_username").clear()
            driver.find_element_by_id("input_username").send_keys("createadmin")
            driver.find_element_by_id("input_password").clear()
            driver.find_element_by_id("input_password").send_keys("123456")
            driver.find_element_by_id("login_btn").click()
            time.sleep(5)
            driver.find_element_by_css_selector("span.user-info").click()
            time.sleep(1)
            driver.find_element_by_link_text(u"退出").click()
            time.sleep(2)
            ###########################################
            # 后置条件: 清理创建用户,有助多次测试
            ###########################################
            driver.find_element_by_id("input_username").clear()
            driver.find_element_by_id("input_username").send_keys("admin")
            driver.find_element_by_id("input_password").clear()
            driver.find_element_by_id("input_password").send_keys("admin123")
            driver.find_element_by_id("login_btn").click()
            time.sleep(5)
            driver.find_element_by_link_text(u"用户管理").click()
            time.sleep(1)
            driver.find_element_by_link_text(u"管理员").click()
            time.sleep(3)
            driver.find_element_by_css_selector("input.form-control.input-sm").clear()
            driver.find_element_by_css_selector("input.form-control.input-sm").send_keys("createadmin")
            time.sleep(5)
            if web_type == 'firefox':
                driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div[2]/"
                                             "div[2]/div[2]/div/table/thead/tr/th[1]/label/input").click()
            elif web_type == 'chrome':
                element = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div[2]/"
                                             "div[2]/div[2]/div/table/thead/tr/th[1]/label/input")
                webdriver.ActionChains(driver).move_to_element(element).click().perform()
            time.sleep(3)
            driver.find_element_by_id("delete_users").click()
            time.sleep(3)
            driver.find_element_by_id("confirm_delete").click()
            time.sleep(3)
            driver.quit()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()