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


from  testcase00_bazaarweb import testcase00_bazaarwebdemo
#from testcase_api_account_adminlogin import testcase_api_account_adminlogin

if __name__ == '__main__':  
    
    #instance unittest object for bazaar marketplace
    suite = unittest.TestSuite()  


#     suite.addTest(get_order_list('test_get_order_list'))
    suite.addTest(testcase00_bazaarweb('test_bazaar_web'))
    #suite.addTest(testcase_api_account_adminlogin('test_testcase_api_account_adminlogin'))

    #outfile=open("c://edaixi_testdata//report.html",'wb')
    #filename = 'G:\\seleniums\\result.html'
    currenttime=time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
    print currenttime
    #fp = file("/usr/edaixi_report/"+currenttime+"caiwu_test_report.html", 'wb')
    fp = file("C:\\JetBrainsPySpace\\test-web\\test-report\\"+currenttime+"bazaar_account_test_report.html", 'wb')
    #fp = file("c:\\edaixi_testdata\\20150717caiwu_test_report.html", 'wb')

    htmlRunner= HTMLTestRunner.HTMLTestRunner(stream=fp,title="HPE Cloud Bazaar Account&Access management story testing result",description="201512 luke")
    #suite =  unittest.TestLoader().loadTestsFromTestCase(MyTest)  
    htmlRunner.run(suite)
    fp.close()
    
 
    
    

    