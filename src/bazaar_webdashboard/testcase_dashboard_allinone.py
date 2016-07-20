# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestcaseDashboardAllinone(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://10.33.206.10"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_case_dashboard_allinone(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        # ERROR: Caught exception [Error: locator strategy either id or name must be specified explicitly.]
        driver.find_element_by_css_selector("span").click()
        driver.find_element_by_id("editPassword").clear()
        driver.find_element_by_id("editPassword").send_keys("a93E6A")
        driver.find_element_by_id("editEnterpriseEmail").clear()
        driver.find_element_by_id("editEnterpriseEmail").send_keys("ibmcuijun2010@126.com")
        driver.find_element_by_id("editPassword").clear()
        driver.find_element_by_id("editPassword").send_keys("Hpe2test")
        driver.find_element_by_id("editSubmit").click()
        time.sleep(2)
        driver.find_element_by_css_selector("a.dropdown-toggle.panelItem > span").click()
        driver.find_element_by_link_text(u"云主机").click()
        driver.find_element_by_css_selector("a.dropdown-toggle.panelItem > span").click()
        driver.find_element_by_link_text(u"负载均衡").click()
        driver.find_element_by_css_selector("a.dropdown-toggle.panelItem > span").click()
        driver.find_element_by_link_text(u"防火墙").click()
        driver.find_element_by_css_selector("a.dropdown-toggle.panelItem > span").click()
        driver.find_element_by_link_text(u"公网IP").click()
        driver.find_element_by_css_selector("a.dropdown-toggle.panelItem > span").click()
        driver.find_element_by_link_text(u"云硬盘").click()
        driver.find_element_by_xpath("//li[2]/a/span").click()
        driver.find_element_by_link_text(u"互联网应用").click()
        driver.find_element_by_xpath("//li[2]/a/span").click()
        driver.find_element_by_link_text(u"大数据").click()
        driver.find_element_by_xpath("//li[2]/a/span").click()
        driver.find_element_by_link_text(u"游戏").click()
        driver.find_element_by_xpath("//li[2]/a/span").click()
        driver.find_element_by_link_text(u"游戏").click()
        driver.find_element_by_xpath("//li[2]/a/span").click()
        driver.find_element_by_link_text("IoT").click()
        driver.find_element_by_xpath("//li[2]/a/span").click()
        driver.find_element_by_link_text(u"移动端").click()
        driver.find_element_by_xpath("//li[2]/a/span").click()
        driver.find_element_by_link_text(u"协同合作").click()
        driver.find_element_by_xpath("//nav/div/ul/li[3]/a/span").click()
        driver.find_element_by_xpath("//span[5]").click()
        driver.find_element_by_css_selector("div.contentbox4 > a > div.bottom > span").click()
        driver.find_element_by_xpath("//nav/div/ul/li[4]/a/span").click()
        driver.find_element_by_xpath("//li[5]/a/span").click()
        driver.find_element_by_xpath("//nav/div/ul/li[6]/a/span").click()
        driver.find_element_by_css_selector("li.language > a > span").click()
        driver.find_element_by_css_selector("ul.clearfix > li > a > span").click()
        # ERROR: Caught exception [Error: locator strategy either id or name must be specified explicitly.]
        driver.find_element_by_xpath("//footer/div/ul/li[3]/a/span").click()
        driver.find_element_by_xpath("//footer/div/ul/li[4]/a/span").click()
        driver.find_element_by_xpath("//li[4]/a/span").click()
        driver.find_element_by_id("$childMenu->nameStringId").click()
        driver.find_element_by_link_text(u"虚拟网络").click()
        driver.find_element_by_link_text(u"公网IP").click()
        driver.find_element_by_link_text(u"路由").click()
        driver.find_element_by_link_text(u"防火墙").click()
        driver.find_element_by_link_text(u"负载均衡").click()
        driver.find_element_by_link_text(u"网络拓扑").click()
        driver.find_element_by_link_text(u"云硬盘").click()
        driver.find_element_by_link_text(u"安全组").click()
        driver.find_element_by_link_text(u"SSH秘钥").click()
        driver.find_element_by_xpath(u"//a[contains(text(),'订单管理')]").click()
        driver.find_element_by_xpath(u"//a[contains(text(),'续费管理')]").click()
        driver.find_element_by_link_text(u"消费记录").click()
        driver.find_element_by_link_text(u"账单管理").click()
        driver.find_element_by_link_text(u"告警规则").click()
        driver.find_element_by_css_selector("a.switch > img").click()
        driver.find_element_by_id("$childMenu->nameStringId").click()
        driver.find_element_by_link_text(u"虚拟网络").click()
        driver.find_element_by_link_text(u"公网IP").click()
        driver.find_element_by_link_text(u"路由").click()
        driver.find_element_by_link_text(u"防火墙").click()
        driver.find_element_by_link_text(u"负载均衡").click()
        driver.find_element_by_link_text(u"网络拓扑").click()
        driver.find_element_by_link_text(u"云硬盘").click()
        driver.find_element_by_xpath(u"//a[contains(text(),'订单管理')]").click()
        driver.find_element_by_link_text(u"企业信息").click()
        driver.find_element_by_link_text(u"用户管理").click()
        driver.find_element_by_link_text(u"消费记录").click()
        driver.find_element_by_link_text(u"收支明细").click()
        driver.find_element_by_link_text(u"账单管理").click()
        driver.find_element_by_link_text(u"告警规则").click()
        driver.find_element_by_id("overview").click()
        driver.find_element_by_id("tabAnalysisCosts").click()
        driver.find_element_by_xpath("//button[@type='button']").click()
        driver.find_element_by_id("timeSelect").click()
        driver.find_element_by_link_text(u"过去6个月").click()
    
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
