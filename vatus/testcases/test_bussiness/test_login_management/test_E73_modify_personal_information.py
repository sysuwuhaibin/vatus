# -*- coding: utf-8 -*-
import time
import unittest
from selenium import webdriver
import settings


class ModifyPersonalInfo(unittest.TestCase):
    def setUp(self):
        self.driver = None
        self.base_url = settings.test_parameters.get("bussiness_base_url")
    
    def test_E73_modify_personal_information(self):
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
            time.sleep(3)
            ###########################################
            # 步骤1：邮箱地址为空
            ###########################################
            driver.find_element_by_css_selector("span.user-info").click()
            driver.find_element_by_link_text(u"个人信息").click()
            time.sleep(3)
            driver.find_element_by_id("email").click()
            driver.find_element_by_css_selector("span.editable-clear-x").click()
            driver.find_element_by_xpath("//button[@type='submit']").click()
            self.assertEqual("请输入邮箱地址！", driver.find_element_by_class_name("editable-error-block").text)
            time.sleep(2)
            ###########################################
            # 步骤2：邮箱地址长度和格式不对
            ###########################################
            driver.find_element_by_css_selector("input.form-control.input-sm").clear()
            driver.find_element_by_css_selector("input.form-control.input-sm").\
                send_keys("123456789012345678901234567890123456789012345678901234567890@1234567890.com")
            driver.find_element_by_xpath("//button[@type='submit']").click()
            self.assertEqual("长度不超过64个字", driver.find_element_by_class_name("editable-error-block").text)
            time.sleep(2)
            driver.find_element_by_css_selector("span.editable-clear-x").click()
            driver.find_element_by_css_selector("input.form-control.input-sm").clear()
            driver.find_element_by_css_selector("input.form-control.input-sm").send_keys("fss@#$%.com")
            driver.find_element_by_xpath("//button[@type='submit']").click()
            self.assertEqual("邮件格式不正确", driver.find_element_by_class_name("editable-error-block").text)
            time.sleep(2)
            ###########################################
            # 步骤3：输入已被其他 用户注册使用的邮箱
            ###########################################
            driver.find_element_by_css_selector("span.editable-clear-x").click()
            driver.find_element_by_css_selector("input.form-control.input-sm").clear()
            driver.find_element_by_css_selector("input.form-control.input-sm").send_keys("staff@example.com")
            driver.find_element_by_xpath("//button[@type='submit']").click()
            time.sleep(2)
            self.assertEqual("邮件地址已被使用", driver.find_element_by_class_name("gritter-without-image").
                             find_element_by_tag_name("p").text)
            time.sleep(8)
            ###########################################
            # 步骤4：输入合法邮箱地址
            ###########################################
            driver.find_element_by_id("email").click()
            driver.find_element_by_css_selector("span.editable-clear-x").click()
            driver.find_element_by_css_selector("input.form-control.input-sm").clear()
            driver.find_element_by_css_selector("input.form-control.input-sm").send_keys("helloworld@java.com")
            driver.find_element_by_xpath("//button[@type='submit']").click()
            time.sleep(2)
            self.assertEqual("用户 admin 信息修改成功", driver.find_element_by_class_name("gritter-without-image").
                             find_element_by_tag_name("p").text)
            time.sleep(8)
            ###########################################
            # 后置条件: 恢复初始邮箱地址,有助多次测试
            ###########################################
            driver.find_element_by_id("email").click()
            driver.find_element_by_css_selector("span.editable-clear-x").click()
            driver.find_element_by_css_selector("input.form-control.input-sm").clear()
            driver.find_element_by_css_selector("input.form-control.input-sm").send_keys("admin@example.com")
            driver.find_element_by_xpath("//button[@type='submit']").click()
            time.sleep(2)
            driver.quit()

if __name__ == "__main__":
    unittest.main()
