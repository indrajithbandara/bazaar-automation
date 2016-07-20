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

class testcase_bazaar_management_productpkg(unittest.TestCase):
    def setUp(self):
        self.driver = bazaar_management_appobject.GetInstance()
        #self.driver = webdriver.Chrome()
        # chromepath=os.path.abspath(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
        #self.driver = webdriver.Chrome()
        #self.driver.implicitly_wait(30)
        print " the bazaarwebhostname is ->",bazaar_management_appobject.bazaaradminhostname
        print " the bazaarwebusername is ->",bazaar_management_appobject.bazaaradminusername
        print " the bazaarwebpassword is ->",bazaar_management_appobject.bazaaradminpassword
        self.base_url = bazaar_management_appobject.bazaaradminhostname
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_bazaar_management_productpkg(self):
        driver = self.driver
        driver.get(self.base_url + "/")
#         driver.find_element_by_id("kw").click()
        driver.implicitly_wait(30)
        print " starting the bazaar title page name is ",driver.title
        #driver.find_element_by_css_selector("a.dropdown-toggle.panelItem > span").click()
        driver.find_element_by_css_selector("span").click()
        time.sleep(1)
        driver.find_element_by_id("editPassword").clear()
        driver.find_element_by_id("editPassword").send_keys(bazaar_management_appobject.bazaaradminpassword)
        driver.implicitly_wait(30)
        driver.find_element_by_id("editEnterpriseEmail").clear()
        driver.find_element_by_id("editEnterpriseEmail").send_keys(bazaar_management_appobject.bazaaradminusername)
        driver.implicitly_wait(30)
        driver.find_element_by_id("editSubmit").click()
        time.sleep(2)

        driver.find_element_by_id("pre").click()
        time.sleep(1)
        driver.find_element_by_name("name").clear()
        driver.find_element_by_name("name").send_keys("test0001product001")
        time.sleep(1)
        driver.find_element_by_css_selector("textarea[name=\"description\"]").clear()
        driver.find_element_by_css_selector("textarea[name=\"description\"]").send_keys("swesdwedwedwedwedwedwe")
        time.sleep(1)
        driver.find_element_by_xpath("(//input[@name='presetTag'])[2]").click()
        time.sleep(1)
        driver.find_element_by_id("btnPresetDefine").click()
        assert driver.title in "HP Cloud"
        time.sleep(2)
        driver.find_element_by_id("productManagementCollapseList").click()
        assert driver.title in "HP Cloud"
        time.sleep(1)
        print " the bazaar title page name is ",driver.title
        driver.find_element_by_xpath("//a[2]/span").click()
        time.sleep(1)
        driver.find_element_by_xpath("//a[3]/span").click()
        time.sleep(1)
        driver.find_element_by_xpath("//a[4]/span").click()
        # ERROR: Caught exception [Error: locator strategy either id or name must be specified explicitly.]
        time.sleep(1)
        driver.find_element_by_xpath("//a[5]/span").click()
        time.sleep(1)
        driver.find_element_by_xpath("//a[6]/span").click()
        time.sleep(1)
        driver.find_element_by_xpath("//a[7]/span").click()
        time.sleep(1)
        driver.find_element_by_xpath("//a[6]/span").click()
        time.sleep(1)
        driver.find_element_by_xpath("//a[5]/span").click()
        time.sleep(1)
        driver.find_element_by_xpath("//a[4]/span").click()
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
