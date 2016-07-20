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

class testcase_bazaar_dashboard_baseprice(unittest.TestCase):
    def setUp(self):
        self.driver = bazaar_management_appobject.GetInstance()
        #self.driver = webdriver.Chrome()
        # chromepath=os.path.abspath(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
        #self.driver = webdriver.Chrome()
        #self.driver.implicitly_wait(30)
        self.base_url = "http://10.33.206.10"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_bazaar_dashboard_baseprice(self):
        driver = self.driver
        driver.get(self.base_url + "/")
#         driver.find_element_by_id("kw").click()
        driver.implicitly_wait(30)
        print " starting the bazaar title page name is ",driver.title
        #driver.find_element_by_css_selector("a.dropdown-toggle.panelItem > span").click()
        driver.find_element_by_css_selector("span").click()
        time.sleep(1)
        driver.find_element_by_id("editPassword").clear()
        driver.find_element_by_id("editPassword").send_keys("Hpe2test")
        driver.implicitly_wait(30)
        driver.find_element_by_id("editEnterpriseEmail").clear()
        driver.find_element_by_id("editEnterpriseEmail").send_keys("jun.cui+0629@hpetest.com")
        driver.implicitly_wait(30)
        driver.find_element_by_id("editSubmit").click()
        time.sleep(2)
        driver.find_element_by_css_selector("a.dropdown-toggle.panelItem > span").click()
        time.sleep(2)
        driver.find_element_by_link_text(u"云主机").click()
        time.sleep(2)

        driver.find_element_by_css_selector("a.dropdown-toggle.panelItem > span").click()
        driver.find_element_by_link_text(u"负载均衡").click()
        time.sleep(2)
        driver.find_element_by_css_selector("a.dropdown-toggle.panelItem > span").click()
        driver.find_element_by_link_text(u"防火墙").click()
        time.sleep(2)
        driver.find_element_by_css_selector("a.dropdown-toggle.panelItem > span").click()
        driver.find_element_by_link_text(u"公网IP").click()
        time.sleep(2)
        driver.find_element_by_xpath("//li[2]/a/span").click()
        time.sleep(2)
        driver.find_element_by_css_selector("a.dropdown-toggle.panelItem > span").click()
        driver.find_element_by_link_text(u"云硬盘").click()
        time.sleep(2)
        
        driver.find_element_by_css_selector("a.dropdown-toggle.panelItem > span").click()
        driver.find_element_by_link_text(u"云硬盘").click()
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
        assert driver.title in "HP Cloud"
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
