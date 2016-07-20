# -*- coding: utf-8 -*-
#encoding:utf-8

# /**
#  * Bazaar automation framework is desined to provide marketplace,dashboard,management web portal,and mobile app,VDI testing
#  * different service providers like HOS,HDP,AWS or Azure with HTTP restful way.
#  *
#  * @author jun.cui@hpe.com
#  * @date: 2016/07/05
#  */
import os
#from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
import bazaar_management_appobject

class testcase_bazaar_management_discount(unittest.TestCase):
    def setUp(self):
        self.driver = bazaar_management_appobject.GetInstance()
        #self.driver = webdriver.Chrome()
        # chromepath=os.path.abspath(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
        #self.driver = webdriver.Chrome()
        #self.driver.implicitly_wait(30)
        self.base_url = "http://10.33.206.10:8190"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_bazaar_management_discount(self):
        driver = self.driver
        driver.get(self.base_url + "/")
#         driver.find_element_by_id("kw").click()
        driver.implicitly_wait(30)
        print " starting the bazaar title page name is ",driver.title
        #driver.find_element_by_css_selector("a.dropdown-toggle.panelItem > span").click()
        driver.find_element_by_css_selector("span").click()
        time.sleep(1)
        driver.find_element_by_id("editPassword").clear()
        driver.find_element_by_id("editPassword").send_keys("Hpe1234!")
        driver.implicitly_wait(30)
        driver.find_element_by_id("editEnterpriseEmail").clear()
        driver.find_element_by_id("editEnterpriseEmail").send_keys("admin@hpe.com")
        driver.implicitly_wait(30)
        driver.find_element_by_id("editSubmit").click()
        time.sleep(2)

        driver.find_element_by_id("priceManagementCollapseList").click()
        time.sleep(2)
        driver.find_element_by_id("createRatingPlan").click()
        time.sleep(2)
        driver.find_element_by_id("planName").clear()
        driver.find_element_by_id("planName").send_keys("cao")
        driver.find_element_by_id("planDesc").clear()
        driver.find_element_by_id("planDesc").send_keys("cao")
        time.sleep(2)
        driver.find_element_by_id("createRatingPlanSubmit").click()
        time.sleep(2)
        driver.find_element_by_id("priceManagementCollapseList").click()
        time.sleep(2)
        driver.find_element_by_id("checkAllRatingPlans").click()
        driver.find_element_by_id("deleteMore").click()
        driver.find_element_by_id("deleteRatingPlanSubmit").click()
        time.sleep(2)
        driver.find_element_by_id("priceManagementCollapseList").click()
        time.sleep(2)
        driver.find_element_by_id("createRatingPlan").click()
        time.sleep(2)
        driver.find_element_by_id("planName").clear()
        driver.find_element_by_id("planName").send_keys("ca")
        driver.find_element_by_id("createRatingPlanSubmit").click()
        time.sleep(2)
        driver.find_element_by_id("planDesc").clear()
        driver.find_element_by_id("planDesc").send_keys("ca")
        driver.find_element_by_id("createRatingPlanSubmit").click()
        time.sleep(2)
        driver.find_element_by_id("priceManagementCollapseList").click()
        time.sleep(2)
        driver.find_element_by_link_text(u"编辑").click()
        time.sleep(2)
        driver.find_element_by_xpath("(//input[@id='planName'])[2]").clear()
        driver.find_element_by_xpath("(//input[@id='planName'])[2]").send_keys("ca1111")
        time.sleep(1)
        driver.find_element_by_id("modifyRatingPlanSubmit").click()
        time.sleep(2)
        driver.find_element_by_id("priceManagementCollapseList").click()
        time.sleep(2)
        driver.find_element_by_xpath(u"(//a[contains(text(),'折扣设置')])[2]").click()
        driver.find_element_by_name("familyId").click()
        time.sleep(2)
        driver.find_element_by_id("checkbox_all").click()
        time.sleep(2)
        driver.find_element_by_id("discountForAllBaseProduct").click()
        time.sleep(2)
        driver.find_element_by_css_selector("div.col-xs-8.inputValue > #editRatingPlanDiscount").clear()
        driver.find_element_by_css_selector("div.col-xs-8.inputValue > #editRatingPlanDiscount").send_keys("1.2")
        time.sleep(1)
        driver.find_element_by_id("discountForAllSubmit").click()
        time.sleep(2)
        driver.find_element_by_css_selector("div.col-xs-8.inputValue > #editRatingPlanDiscount").clear()
        driver.find_element_by_css_selector("div.col-xs-8.inputValue > #editRatingPlanDiscount").send_keys("0.2")
        time.sleep(1)
        driver.find_element_by_id("discountForAllSubmit").click()
        time.sleep(2)
#         driver.find_element_by_id("priceManagementCollapseList").click()
        
#         driver.implicitly_wait(30)
#         driver.find_element_by_id("vm").click()
#         driver.implicitly_wait(30)
#         driver.find_element_by_id("loadBalance").click()
#         driver.implicitly_wait(30)
#         driver.find_element_by_id("firewall").click()
#         driver.implicitly_wait(30)
# 
#         driver.find_element_by_id("publicIp").click()
#         driver.implicitly_wait(30)
#         driver.find_element_by_id("publicIp").click()
#         driver.find_element_by_id("disc").click()
#         driver.implicitly_wait(30)
#         
#         time.sleep(2)
#         driver.find_element_by_css_selector("a.dropdown-toggle.panelItem > span").click()
#         time.sleep(2)
#         driver.find_element_by_link_text(u"云硬盘").click()
#         
#         time.sleep(2)
    
        print " the bazaar title page name is ",driver.title
#         assert driver.title in "HP Cloud"
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except Exception, e: return False
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
