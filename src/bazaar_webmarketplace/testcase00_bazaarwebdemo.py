# -*- coding: utf-8 -*-
#encoding:utf-8
import os
#from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
import bazaar_marketplace_appobject

class testcase00_bazaarweb(unittest.TestCase):
    def setUp(self):
        self.driver = bazaar_marketplace_appobject.GetInstance()
        #self.driver = webdriver.Chrome()
        # chromepath=os.path.abspath(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
        #self.driver = webdriver.Chrome()
        #self.driver.implicitly_wait(30)
        self.base_url = "http://10.33.206.10"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_bazaar_web(self):
        driver = self.driver
        driver.get(self.base_url + "/")
#         driver.find_element_by_id("kw").click()
        driver.implicitly_wait(30)
        print " starting the bazaar title page name is ",driver.title
        driver.find_element_by_css_selector("a.dropdown-toggle.panelItem > span").click()
        driver.find_element_by_link_text(u"云主机").click()
        driver.implicitly_wait(60)
        driver.find_element_by_name("name").click()

#         driver.find_element_by_id("pre").click()
#         driver.implicitly_wait(60)
#         driver.find_element_by_id("publicIpInput").click()
#         driver.implicitly_wait(60)

        driver.find_element_by_link_text(u"按量付费").click()
        driver.find_element_by_id("showAdvanced").click()
        driver.find_element_by_id("addDiscBtn").click()
        driver.implicitly_wait(60)
        driver.find_element_by_css_selector("div.discItem > input[name=\"name\"]").click()
        driver.implicitly_wait(60)
        driver.find_element_by_id("submit").click()
        driver.implicitly_wait(60)
        driver.find_element_by_id("agreement").click()
        driver.implicitly_wait(60)
        driver.find_element_by_id("open").click()
        driver.implicitly_wait(60)
        driver.find_element_by_link_text(u"继续订购").click()
    
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
