# -*- coding: utf-8 -*-
#encoding:utf-8 
# /**
#  * ServiceAdapter is desined to provide unique access methods for upper commponents by adapting
#  * different service providers like HOS,HDP,AWS or Azure with HTTP restful way.
#  *
#  * @author jia.zou@hpe.com
#  * @date: 2015/12/14
#  */
 
import unittest, time, re 
import HTMLTestRunner


from  testcase00_bazaar_management_productpkg import testcase_bazaar_management_productpkg
from  testcase01_bazaar_management_imagesyn  import testcase_bazaar_management_imagesyn
from  testcase04_bazaar_management_discount import testcase_bazaar_management_discount
from  testcase05_bazaar_dashboard_exception import testcase_bazaar_dashboard_exception
#from testcase_api_account_adminlogin import testcase_api_account_adminlogin

if __name__ == '__main__':  
    #suite = unittest.TestSuite()  

    suite= unittest.TestSuite()  

#     suite.addTest(get_order_list('test_get_order_list'))
#     suite.addTest(testcase_bazaar_management_productpkg('test_bazaar_management_productpkg'))
#     suite.addTest(testcase_bazaar_management_imagesyn('test_bazaar_management_imagesyn'))
#     suite.addTest(testcase_bazaar_management_discount('test_bazaar_management_discount'))
    suite.addTest(testcase_bazaar_dashboard_exception('test_bazaar_dashboard_exception'))
    #suite.addTest(testcase_api_account_adminlogin('test_testcase_api_account_adminlogin'))

    #outfile=open("c://edaixi_testdata//report.html",'wb')
    #filename = 'G:\\seleniums\\result.html'
    currenttime=time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
    print currenttime
    #fp = file("/usr/edaixi_report/"+currenttime+"caiwu_test_report.html", 'wb')
    fp = file("C:\\BazaarCodeDeveloper\\bazaarworkspace\\bazaar-automation\\test-report\\"+currenttime+"bazaar_management_test_report.html", 'wb')
    #fp = file("c:\\edaixi_testdata\\20150717caiwu_test_report.html", 'wb')

    htmlRunner= HTMLTestRunner.HTMLTestRunner(stream=fp,title="HPE Cloud Bazaar Management testing result",description="20160708 luke (contact mail:jun.cui@hpe.com)")
    #suite =  unittest.TestLoader().loadTestsFromTestCase(MyTest)  
    htmlRunner.run(suite)
    fp.close()
    
 
    
    

    