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
import bazaar_dashboard_appobject

class testcase_bazaar_dashboard_vm_create_lifecycle(unittest.TestCase):
    def setUp(self):
        self.driver = bazaar_dashboard_appobject.GetInstance()
        #self.driver = webdriver.Chrome()
        # chromepath=os.path.abspath(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
        #self.driver = webdriver.Chrome()
        #self.driver.implicitly_wait(30)
        print " the bazaarwebhostname is ->",bazaar_dashboard_appobject.bazaarwebhostname
        print " the bazaarwebusername is ->",bazaar_dashboard_appobject.bazaarwebusername
        print " the bazaarwebpassword is ->",bazaar_dashboard_appobject.bazaarwebpassword
        self.base_url = bazaar_dashboard_appobject.bazaarwebhostname
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_bazaar_dashboard_vm_create_lifecycle(self):
        driver = self.driver
        driver.get(self.base_url + "/")
#         driver.find_element_by_id("kw").click()
        driver.implicitly_wait(30)
        print " starting the bazaar title page name is ",driver.title
        #driver.find_element_by_css_selector("a.dropdown-toggle.panelItem > span").click()
        driver.find_element_by_css_selector("span").click()
        time.sleep(1)
        driver.find_element_by_id("editPassword").clear()
        driver.find_element_by_id("editPassword").send_keys(bazaar_dashboard_appobject.bazaarwebpassword)
        driver.implicitly_wait(30)
        driver.find_element_by_id("editEnterpriseEmail").clear()
        driver.find_element_by_id("editEnterpriseEmail").send_keys(bazaar_dashboard_appobject.bazaarwebusername)
        driver.implicitly_wait(30)
        driver.find_element_by_id("editSubmit").click()
        time.sleep(2)
#         driver.find_element_by_css_selector("a.dropdown-toggle.panelItem > span").click()
#         time.sleep(2)
#         driver.find_element_by_id("editSubmit").click()
        driver.find_element_by_xpath("//li[4]/a/span").click()
        time.sleep(2)
        driver.find_element_by_id("$childMenu->nameStringId").click()
        time.sleep(2)
        driver.find_element_by_id("selectAll").click()
        time.sleep(2)
        driver.find_element_by_id("selectAll").click()
        time.sleep(2)
        driver.find_element_by_id("1000047").click()
        time.sleep(2)
        driver.find_element_by_id("selectmore").click()
        time.sleep(2)
        driver.find_element_by_id("startup").click()
        time.sleep(2)
        driver.find_element_by_id("vmStartSubmit").click()
        time.sleep(2)
        driver.find_element_by_id("$childMenu->nameStringId").click()
        time.sleep(2)
        driver.find_element_by_id("1000047").click()
        time.sleep(2)
        driver.find_element_by_id("selectmore").click()
        time.sleep(2)
        Select(driver.find_element_by_id("selectmore")).select_by_visible_text(u"更多操作")
        time.sleep(3)
        driver.find_element_by_id("vmShutdownSubmit").click()
        time.sleep(3)
        driver.find_element_by_link_text(u"刷新").click()
        time.sleep(2)
        driver.find_element_by_link_text(u"刷新").click()
        time.sleep(2)
        driver.find_element_by_id("1000047").click()
        time.sleep(2)
        driver.find_element_by_id("$childMenu->nameStringId").click()
        time.sleep(2)
        driver.find_element_by_id("1000047").click()
        time.sleep(2)
        driver.find_element_by_id("selectmore").click()
        time.sleep(2)
        Select(driver.find_element_by_id("selectmore")).select_by_visible_text(u"更多操作")
        time.sleep(2)
        driver.find_element_by_id("vmRebootSubmit").click()
        time.sleep(2)
        driver.find_element_by_link_text(u"刷新").click()
        time.sleep(2)
        driver.find_element_by_link_text(u"刷新").click()
        time.sleep(2)
        driver.find_element_by_id("$childMenu->nameStringId").click()
        time.sleep(2)
        driver.find_element_by_id("vmSnapshotButton").click()
        time.sleep(2)

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
