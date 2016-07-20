# -*- coding: utf-8 -*-
#encoding:utf-8 

# /**
#  * Bazaar automation framework is desined to provide marketplace,dashboard,management web portal,and mobile app,VDI testing
#  * different service providers like HOS,HDP,AWS or Azure with HTTP restful way.
#  *
#  * @author jun.cui@hpe.com
#  * @date: 2016/07/05
#  */
 
import unittest, time, re 
import HTMLTestRunner
# from  testcase00_bazaarwebdemo import testcase00_bazaarweb
# from  testcase00_bazaarwebmanagement  import testcase_bazaarwebmangement

from testcase00_bazaar_marketplace_tab01product import testcase_bazaar_marketplace_tab01product
from testcase00_bazaar_marketplace_tab02market import testcase_bazaar_marketplace_tab02market
from testcase00_bazaar_marketplace_tab03solution import testcase_bazaar_marketplace_tab03solution
from testcase00_bazaar_marketplace_tab04service import testcase_bazaar_marketplace_tab04service
from testcase00_bazaar_marketplace_tab05partner import testcase_bazaar_marketplace_tab05partner
from testcase00_bazaar_marketplace_tab06helpcenter import  testcase_bazaar_marketplace_tab06helpcenter
from testcase00_bazaar_marketplace_tab07others import testcase_bazaar_marketplace_tab07others
#from testcase_api_account_adminlogin import testcase_api_account_adminlogin

if __name__ == '__main__':  
    #suite = unittest.TestSuite()  

    suite= unittest.TestSuite()  

#     suite.addTest(get_order_list('test_get_order_list'))
    #suite.addTest(testcase00_bazaarweb('test_bazaar_web'))
    #suite.addTest(testcase_bazaarwebmangement('test_bazaar_webmanagement'))
    suite.addTest(testcase_bazaar_marketplace_tab01product('test_bazaar_marketplace_tab01product'))
    suite.addTest(testcase_bazaar_marketplace_tab02market('test_bazaar_marketplace_tab02market'))
    suite.addTest(testcase_bazaar_marketplace_tab03solution('test_bazaar_marketplace_tab03solution'))
    suite.addTest(testcase_bazaar_marketplace_tab04service('test_bazaar_marketplace_tab04service'))
    suite.addTest(testcase_bazaar_marketplace_tab05partner('test_bazaar_marketplace_tab05partner'))
    suite.addTest(testcase_bazaar_marketplace_tab07others('test_bazaar_marketplace_tab07others'))
    suite.addTest(testcase_bazaar_marketplace_tab06helpcenter('test_bazaar_marketplace_tab06helpcenter'))
    #suite.addTest(testcase_api_account_adminlogin('test_testcase_api_account_adminlogin'))

    #outfile=open("c://edaixi_testdata//report.html",'wb')
    #filename = 'G:\\seleniums\\result.html'
    currenttime=time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
    print currenttime
    #fp = file("/usr/edaixi_report/"+currenttime+"caiwu_test_report.html", 'wb')
    fp = file("C:\\BazaarCodeDeveloper\\bazaarworkspace\\bazaar-automation\\test-report\\"+currenttime+"bazaar_marketplace_test_report.html", 'wb')
    #fp = file("c:\\edaixi_testdata\\20150717caiwu_test_report.html", 'wb')

    htmlRunner= HTMLTestRunner.HTMLTestRunner(stream=fp,title="HPE Cloud Bazaar Marketplace testing result",description="20160707 luke (contact mail:jun.cui@hpe.com)")
    #suite =  unittest.TestLoader().loadTestsFromTestCase(MyTest)  
    htmlRunner.run(suite)
    fp.close()
    
 
    
    

    