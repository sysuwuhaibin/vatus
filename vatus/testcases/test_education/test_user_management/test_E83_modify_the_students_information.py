# -*- coding: utf-8 -*-
import time
import unittest

from selenium import webdriver

import settings


class ModifyStudentInfo(unittest.TestCase):
    def setUp(self):
        self.driver = None
        self.base_url = settings.test_parameters.get("education_base_url")

    def test_E83_modify_the_students_information(self):
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
            # 前置条件：登录系统,创建测试数据
            ###########################################
            driver.find_element_by_id("input_username").clear()
            driver.find_element_by_id("input_username").send_keys(settings.test_parameters.get("admin_username"))
            driver.find_element_by_id("input_password").clear()
            driver.find_element_by_id("input_password").send_keys(settings.test_parameters.get("admin_password"))
            driver.find_element_by_id("login_btn").click()
            time.sleep(5)
            driver.find_element_by_link_text(u"用户管理").click()
            time.sleep(1)
            driver.find_element_by_link_text(u"学生").click()
            time.sleep(3)
            driver.find_element_by_id("create_user").click()
            time.sleep(2)
            driver.find_element_by_id("username").clear()
            driver.find_element_by_id("username").send_keys("student01")
            driver.find_element_by_id("fullname").clear()
            driver.find_element_by_id("fullname").send_keys("student01")
            driver.find_element_by_id("email").clear()
            driver.find_element_by_id("email").send_keys("student01@vinzor.com")
            driver.find_element_by_id("password").clear()
            driver.find_element_by_id("password").send_keys("123456")
            driver.find_element_by_id("confirm").clear()
            driver.find_element_by_id("confirm").send_keys("123456")
            time.sleep(3)
            driver.find_element_by_id("confirm_action").click()
            time.sleep(5)
            ###########################################
            # 步骤1：姓名、邮件输入留空，检查提示
            ###########################################
            driver.find_element_by_css_selector("input.form-control.input-sm").clear()
            driver.find_element_by_css_selector("input.form-control.input-sm").send_keys("student01")
            time.sleep(5)
            if web_type == 'firefox':
                driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/"
                                             "div[2]/div[2]/div[2]/div/table/tbody/tr/td[6]/div/a[1]").click()
            elif web_type == 'chrome':
                element = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/"
                                                       "div[2]/div[2]/div[2]/div/table/tbody/tr/td[6]/div/a[1]")
                webdriver.ActionChains(driver).move_to_element(element).click().perform()
            time.sleep(3)
            self.assertEqual('true', driver.find_element_by_id("username").get_attribute("readonly"))
            driver.find_element_by_id("fullname").clear()
            driver.find_element_by_id("email").clear()
            driver.find_element_by_id("confirm_action").click()
            time.sleep(2)
            self.assertEqual("请输入姓名", driver.find_element_by_id("fullname-error").text)
            self.assertEqual("请输入邮件地址", driver.find_element_by_id("email-error").text)
            ###########################################
            # 步骤2：姓名、邮件输入过长，检查提示
            ###########################################
            driver.find_element_by_id("fullname").clear()
            driver.find_element_by_id("fullname").\
                send_keys("1234567890123456789012345678901234567890123456789012345678901234567890")
            driver.find_element_by_id("email").clear()
            driver.find_element_by_id("email").\
                send_keys("12345678901234567890123456789012345678901234567890@12345678901234567.com")
            driver.find_element_by_id("confirm_action").click()
            time.sleep(2)
            self.assertEqual("长度不超过64个字", driver.find_element_by_id("fullname-error").text)
            self.assertEqual("长度1-64个字", driver.find_element_by_id("email-error").text)
            ###########################################
            # 步骤3：邮箱编辑输入格式不正确，检查提示
            ###########################################
            driver.find_element_by_id("email").clear()
            driver.find_element_by_id("email").send_keys("test@@dfd.com")
            driver.find_element_by_id("confirm_action").click()
            time.sleep(2)
            self.assertEqual("请输入有效的电子邮件地址", driver.find_element_by_id("email-error").text)
            ###########################################
            # 步骤4：邮箱已被其他用户使用，检查提示
            ###########################################
            driver.find_element_by_id("fullname").clear()
            driver.find_element_by_id("fullname").send_keys("vinzor")
            driver.find_element_by_id("email").clear()
            driver.find_element_by_id("email").send_keys("student@example.com")
            driver.find_element_by_id("confirm_action").click()
            time.sleep(2)
            self.assertEqual("邮件地址已被使用", driver.find_element_by_id("email-error").text)
            ###########################################
            # 步骤5：正常合理输入，成功编辑
            ###########################################
            driver.find_element_by_id("email").clear()
            driver.find_element_by_id("email").send_keys("test11@vinzor.com")
            driver.find_element_by_id("confirm_action").click()
            time.sleep(3)
            self.assertEqual("用户 student01 信息修改成功", driver.find_element_by_class_name("gritter-without-image").
                             find_element_by_tag_name("p").text)
            ###########################################
            # 后置条件: 清理创建用户,有助多次测试
            ###########################################
            driver.find_element_by_css_selector("input.form-control.input-sm").clear()
            driver.find_element_by_css_selector("input.form-control.input-sm").send_keys("student01")
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
            time.sleep(3)
            driver.quit()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
