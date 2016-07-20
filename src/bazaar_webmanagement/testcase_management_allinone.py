# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestcaseManagementAllinone(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://10.33.206.10:8190"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_case_management_allinone(self):
        driver = self.driver
        driver.get(self.base_url + "/")
#         driver.find_element_by_id("nm-international").click()
#         driver.find_element_by_id("nm-society").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.find_element_by_id("editEnterpriseEmail").clear()
        driver.find_element_by_id("editEnterpriseEmail").send_keys("admin@hpe.com")
        driver.find_element_by_id("editPassword").clear()
        driver.find_element_by_id("editPassword").send_keys("Hpe1234!")
        driver.find_element_by_id("editSubmit").click()
        driver.find_element_by_id("productManagementCollapseList").click()
        time.sleep(30) 
        driver.find_element_by_id("productManagementCollapseList").click()
        driver.find_element_by_id("pre").click()
        time.sleep(30) 
        driver.find_element_by_name("name").clear()
        driver.find_element_by_name("name").send_keys("awsqwswqd")
        driver.find_element_by_css_selector("textarea[name=\"description\"]").click()
        driver.find_element_by_css_selector("textarea[name=\"description\"]").clear()
        driver.find_element_by_css_selector("textarea[name=\"description\"]").send_keys("dqwdwqdqw")
        driver.find_element_by_xpath("(//input[@name='presetTag'])[3]").click()
        driver.find_element_by_xpath("(//input[@name='presetTag'])[2]").click()
        driver.find_element_by_id("btnPresetDefine").click()
        driver.find_element_by_id("btnPresetConfirm").click()
        driver.find_element_by_id("savePreset").click()
        driver.find_element_by_id("productManagementCollapseList").click()
        driver.find_element_by_xpath("//input[@id='64']").click()
        Select(driver.find_element_by_id("selectmore")).select_by_visible_text(u"更多操作")
        driver.find_element_by_id("presetPutSubmit").click()
        driver.find_element_by_link_text(u"编辑").click()
        driver.find_element_by_name("name").clear()
        driver.find_element_by_name("name").send_keys("test123wdqwd")
        driver.find_element_by_css_selector("textarea[name=\"description\"]").clear()
        driver.find_element_by_css_selector("textarea[name=\"description\"]").send_keys("wqwdwdqw")
        driver.find_element_by_id("btnPresetDefine").click()
        driver.find_element_by_id("btnPresetConfirm").click()
        driver.find_element_by_id("savePreset").click()
        driver.find_element_by_id("productManagementCollapseList").click()
        driver.find_element_by_link_text(u"异常服务处理").click()
        driver.find_element_by_link_text(u"重新创建").click()
        driver.find_element_by_id("9a34cc11-c703-4d0c-8703-2a360d98d6c4").click()
        driver.find_element_by_id("orderManagementCollapseDetail").click()
        driver.find_element_by_link_text(u"余额管理").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'充值')])[2]").click()
        driver.find_element_by_id("rechargeAmount").clear()
        driver.find_element_by_id("rechargeAmount").send_keys("34567")
        driver.find_element_by_id("rechargeInputSubmit").click()
        driver.find_element_by_id("rechargeConfirmSubmit").click()
        driver.find_element_by_link_text(u"余额管理").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
