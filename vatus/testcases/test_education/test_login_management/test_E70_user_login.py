# -*- coding: utf-8 -*-
import time
import unittest
import win32api

import win32con
from selenium import webdriver

import settings


class Login(unittest.TestCase):
    def setUp(self):
        self.driver = None
        self.base_url = settings.test_parameters.get("education_base_url")
    
    def test_E70_user_login(self):
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
            # 步骤1：用户名密码为空
            ###########################################
            driver.find_element_by_id("input_username").clear()
            driver.find_element_by_id("input_password").clear()
            driver.find_element_by_id("login_btn").click()
            username_text = driver.find_element_by_id("input_username-error").text
            self.assertEqual("用户名不能为空", username_text)
            password_text = driver.find_element_by_id("input_password-error").text
            self.assertEqual("密码不能为空", password_text)
            ###########################################
            # 步骤2：用户名和密码为空格
            ###########################################
            driver.find_element_by_id("input_username").clear()
            driver.find_element_by_id("input_username").send_keys("   ")
            driver.find_element_by_id("input_password").clear()
            driver.find_element_by_id("input_password").send_keys(" ")
            driver.find_element_by_id("login_btn").click()
            username_text = driver.find_element_by_id("input_username-error").text
            self.assertEqual("用户名不能为空", username_text)
            password_text = driver.find_element_by_id("input_password-error").text
            self.assertEqual("密码不能为空", password_text)
            ###########################################
            # 步骤3：用户名长度超过64个字符
            ###########################################
            driver.find_element_by_id("input_username").clear()
            driver.find_element_by_id("input_username").send_keys("12345678901234567890123456789012345678901234567890123456789012345")
            driver.find_element_by_id("login_btn").click()
            username_text = driver.find_element_by_id("input_username-error").text
            self.assertEqual("用户名长度为1～64个字", username_text)
            ###########################################
            # 步骤4：密码长度小于5个字符和超过64个字符
            ###########################################
            driver.find_element_by_id("input_password").clear()
            driver.find_element_by_id("input_password").send_keys("12345678901234567890123456789012345678901234567890123456789012345")
            driver.find_element_by_id("login_btn").click()
            password_text = driver.find_element_by_id("input_password-error").text
            self.assertEqual("密码长度为5～64个字", password_text)
            driver.find_element_by_id("input_password").clear()
            driver.find_element_by_id("input_password").send_keys("1234")
            driver.find_element_by_id("login_btn").click()
            password_text = driver.find_element_by_id("input_password-error").text
            self.assertEqual("密码长度为5～64个字", password_text)
            ###########################################
            # 步骤5：输入正确用户名，密码输入错误，点击登录
            ###########################################
            driver.find_element_by_id("input_username").clear()
            driver.find_element_by_id("input_username").send_keys("admin")
            driver.find_element_by_id("input_password").clear()
            driver.find_element_by_id("input_password").send_keys("te$5ffd")
            driver.find_element_by_id("login_btn").click()
            time.sleep(1)
            login_text = driver.find_element_by_id("login_state").text
            self.assertEqual("错误用户名或密码", login_text)
            ###########################################
            # 步骤6：输入不存在的用户名，密码随意
            ###########################################
            driver.find_element_by_id("input_username").clear()
            driver.find_element_by_id("input_username").send_keys("hahaha")
            driver.find_element_by_id("input_password").clear()
            driver.find_element_by_id("input_password").send_keys("admin123")
            driver.find_element_by_id("login_btn").click()
            time.sleep(1)
            login_text = driver.find_element_by_id("login_state").text
            self.assertEqual("错误用户名或密码", login_text)

            caps = win32api.GetKeyState(win32con.VK_CAPITAL)
            if caps == 0 or caps == -128:
                win32api.keybd_event(win32con.VK_CAPITAL, 0, 0, 0)
            ###########################################
            # 步骤7：打开大写键盘
            ###########################################
            driver.find_element_by_id("input_password").clear()
            driver.find_element_by_id("input_password").click()
            win32api.keybd_event(70, 0, 0, 0)
            time.sleep(1)
            login_text = driver.find_element_by_id("login_state").text
            self.assertEqual("键盘大写锁定打开，请注意大小写", login_text)
            caps = win32api.GetKeyState(win32con.VK_CAPITAL)
            if caps == 0 or caps == -128:
                win32api.keybd_event(win32con.VK_CAPITAL, 0, 0, 0)
                win32api.keybd_event(win32con.VK_CAPITAL, 0, win32con.KEYEVENTF_KEYUP, 0)
            else:
                win32api.keybd_event(win32con.VK_CAPITAL, 0, win32con.KEYEVENTF_KEYUP, 0)
                win32api.keybd_event(win32con.VK_CAPITAL, 0, 0, 0)
                win32api.keybd_event(win32con.VK_CAPITAL, 0, win32con.KEYEVENTF_KEYUP, 0)
            ###########################################
            # 步骤8：正确用户名密码
            ###########################################
            driver.find_element_by_id("input_username").clear()
            driver.find_element_by_id("input_username").send_keys(settings.test_parameters.get("admin_username"))
            driver.find_element_by_id("input_password").clear()
            driver.find_element_by_id("input_password").send_keys(settings.test_parameters.get("admin_password"))
            driver.find_element_by_id("login_btn").click()
            # 退出
            time.sleep(5)
            driver.find_element_by_css_selector("span.user-info").click()
            time.sleep(2)
            driver.find_element_by_link_text(u"退出").click()
            driver.quit()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
