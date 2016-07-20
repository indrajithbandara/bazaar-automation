# -*- coding: utf-8 -*-
#encoding:utf-8 
import unittest, time, re 
import HTMLTestRunner


from get_order import *
from create_order import *

if __name__ == '__main__':  
    suite = unittest.TestSuite()  

    suite= unittest.TestSuite()  

#     suite.addTest(get_order_list('test_get_order_list'))
    suite.addTest(get_order('test_get_order'))
    suite.addTest(create_order('test_create_order'))

    #outfile=open("c://edaixi_testdata//report.html",'wb')
    #filename = 'G:\\seleniums\\result.html'
    currenttime=time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
    print currenttime
    #fp = file("/usr/edaixi_report/"+currenttime+"caiwu_test_report.html", 'wb')
    fp = file("C:\\xampp\\htdocs\\bazaar-automation\\test-report\\"+currenttime+"bazaar_account_test_report.html", 'wb')
    #fp = file("c:\\edaixi_testdata\\20150717caiwu_test_report.html", 'wb')

    htmlRunner= HTMLTestRunner.HTMLTestRunner(stream=fp,title="HPE Cloud Bazaar Account&Access management story testing result",description="201512 luke")
    #suite =  unittest.TestLoader().loadTestsFromTestCase(MyTest)  
    htmlRunner.run(suite)
    fp.close()
    
 
    
    

    