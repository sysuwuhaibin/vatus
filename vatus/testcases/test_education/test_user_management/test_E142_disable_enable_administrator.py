# -*- coding: utf-8 -*-
import time
import unittest

from selenium import webdriver

import settings


class DisableEnableAdministrator(unittest.TestCase):
    def setUp(self):
        self.driver = None
        self.base_url = settings.test_parameters.get("education_base_url")

    # chrome 浏览器存在兼容问题
    def test_E142_disable_enable_administrator(self):
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
            # 前置条件：登录系统，创建测试数据
            ###########################################
            driver.find_element_by_id("input_username").clear()
            driver.find_element_by_id("input_username").send_keys(settings.test_parameters.get("admin_username"))
            driver.find_element_by_id("input_password").clear()
            driver.find_element_by_id("input_password").send_keys(settings.test_parameters.get("admin_password"))
            driver.find_element_by_id("login_btn").click()
            time.sleep(5)
            driver.find_element_by_link_text(u"用户管理").click()
            time.sleep(1)
            driver.find_element_by_link_text(u"管理员").click()
            time.sleep(3)
            driver.find_element_by_id("create_user").click()
            time.sleep(1)
            driver.find_element_by_id("username").clear()
            driver.find_element_by_id("username").send_keys("admin01")
            driver.find_element_by_id("fullname").clear()
            driver.find_element_by_id("fullname").send_keys("admin01")
            driver.find_element_by_id("email").clear()
            driver.find_element_by_id("email").send_keys("admin01@vinzor.com")
            driver.find_element_by_id("password").clear()
            driver.find_element_by_id("password").send_keys("123456")
            driver.find_element_by_id("confirm").clear()
            driver.find_element_by_id("confirm").send_keys("123456")
            time.sleep(3)
            driver.find_element_by_id("confirm_action").click()
            time.sleep(5)
            self.assertEqual("用户 admin01 创建成功", driver.find_element_by_class_name("gritter-without-image").
                             find_element_by_tag_name("p").text)
            ###########################################
            # 步骤1：禁用新建用户，新建用户无法登录
            ###########################################
            time.sleep(8)
            driver.find_element_by_css_selector("input.form-control.input-sm").clear()
            driver.find_element_by_css_selector("input.form-control.input-sm").send_keys("admin01")
            time.sleep(5)
            if web_type == 'firefox':
                driver.find_element_by_id("status_btn").click()
            elif web_type == 'chrome':
                continue
                #element = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/table/tbody/tr/td[5]/span/label/input")
                #webdriver.ActionChains(driver).move_to_element(element).click().perform()
            time.sleep(11)

            if web_type == 'firefox':
                driver.find_element_by_id("status_btn").click()
            elif web_type == 'chrome':
                element = driver.find_element_by_id("status_btn")
                webdriver.ActionChains(driver).move_to_element(element).click().perform()
            time.sleep(11)

            if web_type == 'firefox':
                driver.find_element_by_id("status_btn").click()
            elif web_type == 'chrome':
                element = driver.find_element_by_id("status_btn")
                webdriver.ActionChains(driver).move_to_element(element).click().perform()
            time.sleep(11)

            driver.find_element_by_css_selector("span.user-info").click()
            time.sleep(1)
            driver.find_element_by_link_text(u"退出").click()
            time.sleep(2)
            driver.find_element_by_id("input_username").clear()
            driver.find_element_by_id("input_username").send_keys("admin01")
            driver.find_element_by_id("input_password").clear()
            driver.find_element_by_id("input_password").send_keys("123456")
            driver.find_element_by_id("login_btn").click()
            time.sleep(12)
            login_text = driver.find_element_by_id("login_state").text
            self.assertEqual("用户处于禁用状态禁止登录", login_text)
            ###########################################
            # 步骤2：激活新建用户，新建用户可以登录
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
            driver.find_element_by_css_selector("input.form-control.input-sm").send_keys("admin01")
            time.sleep(5)
            if web_type == 'firefox':
                driver.find_element_by_id("status_btn").click()
            elif web_type == 'chrome':
                element = driver.find_element_by_id("status_btn")
                webdriver.ActionChains(driver).move_to_element(element).click().perform()
            time.sleep(11)
            driver.find_element_by_css_selector("span.user-info").click()
            time.sleep(1)
            driver.find_element_by_link_text(u"退出").click()
            time.sleep(2)
            driver.find_element_by_id("input_username").clear()
            driver.find_element_by_id("input_username").send_keys("admin01")
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
            driver.find_element_by_css_selector("input.form-control.input-sm").send_keys("admin01")
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