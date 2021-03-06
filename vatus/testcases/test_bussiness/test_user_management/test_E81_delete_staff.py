# -*- coding: utf-8 -*-
import time
import unittest
from selenium import webdriver
import settings


class DeleteStaff(unittest.TestCase):
    def setUp(self):
        self.driver = None
        self.base_url = settings.test_parameters.get("bussiness_base_url")

    def test_E81_delete_staff(self):
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
            driver.find_element_by_id("input_username").send_keys("admin")
            driver.find_element_by_id("input_password").clear()
            driver.find_element_by_id("input_password").send_keys("admin123")
            driver.find_element_by_id("login_btn").click()
            time.sleep(5)
            driver.find_element_by_link_text(u"用户管理").click()
            time.sleep(1)
            driver.find_element_by_link_text(u"员工").click()
            time.sleep(3)
            student_names = ['deletestaff01','deletestaff02','deletestaff03','deletestaf04']
            for staff_name in student_names:
                driver.find_element_by_id("create_user").click()
                time.sleep(2)
                driver.find_element_by_id("username").clear()
                driver.find_element_by_id("username").send_keys(staff_name)
                driver.find_element_by_id("fullname").clear()
                driver.find_element_by_id("fullname").send_keys(staff_name)
                driver.find_element_by_id("email").clear()
                driver.find_element_by_id("email").send_keys(staff_name+"@vinzor.com")
                driver.find_element_by_id("password").clear()
                driver.find_element_by_id("password").send_keys("123456")
                driver.find_element_by_id("confirm").clear()
                driver.find_element_by_id("confirm").send_keys("123456")
                time.sleep(3)
                driver.find_element_by_id("confirm_action").click()
                time.sleep(5)
            ###########################################
            # 步骤1：未勾选任何一条学生记录，点击“删除”按钮
            ###########################################
            time.sleep(5)
            driver.find_element_by_id("delete_user").click()
            time.sleep(1)
            self.assertEqual("请选择一个或多个要删除的用户", driver.find_element_by_class_name("gritter-without-image").
                             find_element_by_tag_name("p").text)
            time.sleep(8)
            ###########################################
            # 步骤2：多选删除
            ###########################################
            driver.find_element_by_css_selector("input.form-control.input-sm").clear()
            driver.find_element_by_css_selector("input.form-control.input-sm").send_keys("deletestaff")
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
            ###########################################
            # 步骤3：单选删除
            ###########################################
            driver.find_element_by_css_selector("input.form-control.input-sm").clear()
            driver.find_element_by_css_selector("input.form-control.input-sm").send_keys("deletestaf")
            time.sleep(5)
            driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div[2]/"
                                         "div[2]/div[2]/div/table/tbody/tr/td[5]/div/a[2]").click()
            time.sleep(3)
            driver.find_element_by_id("confirm_delete").click()
            time.sleep(3)
            ###########################################
            # 步骤4：弹出删除框，但是取消
            ###########################################
            driver.find_element_by_link_text(u"员工").click()
            time.sleep(1)
            driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div[2]/"
                                         "div[2]/div[2]/div/table/tbody/tr/td[5]/div/a[2]").click()
            time.sleep(5)
            driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/"
                                         "table/tbody/tr/td[5]/div/a[2]").click()
            time.sleep(3)

            driver.quit()


if __name__ == "__main__":
    unittest.main()
