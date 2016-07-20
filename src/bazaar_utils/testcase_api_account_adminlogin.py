# -*- coding: utf-8 -*-
#encoding:utf-8 
import httplib
import unittest

import urllib 
import urllib2 




class testcase_api_account_adminlogin(unittest.TestCase):
    def setUp(self):
        #self.widget = Widget('The widget')
        httpClient = None
        self.httpClient = httplib.HTTPConnection('openapi.baidu.com', 80, timeout=10)
        
    def tearDown(self):
        #self.widget.dispose()
        #self.widget = None
        self.httpClient.close()
        
    def test_testcase_api_account_httpssldemo(self):
            url = 'http://www.pythontab.com' 
            user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' 
  
            values = {'name' : 'Michael Foord',
           'location' : 'pythontab',
           'language' : 'Python' } 
            headers = { 'User-Agent' : user_agent } 
            data = urllib.urlencode(values) 
            req = urllib2.Request(url, data, headers) 
            response = urllib2.urlopen(req) 
            the_page = response.read()
            
    #change user interface for bazaar_utils & access story
    def test_testcase_api_account_adminlogin(self):
        try:
            
            self.httpClient.request('GET', '/rest/2.0/passport/users/getInfo?session_key=9XNNXe66zOlSassjSKD5gry9BiN61IUEi8IpJmjBwvU07RXP0J3c4GnhZR3GKhMHa1A%3D&timestamp=2011-06-21+17%3A18%3A09&format=json&uid=67411167&sign=d24dd357a95a2579c410b3a92495f009 HTTP/1.1')
            #response是HTTPResponse对象
            response = self.httpClient.getresponse()
            print response.status
            statucode=response.status
            print response.read()
            if statucode=='200' or statucode=='201':
                print "The get_order_list status is 200 or 201"
            else:
                raise "The get_order_list has exception"
                print response.reason
                print response.read()
            #self.assertEqual(statucode, 200,'incorrect default size')
        except Exception, e:
            print e
        #finally:
            #if self.httpClient:
               #self.httpClient.close()


