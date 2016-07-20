'''
Created on Apr 21, 2016

@author: cuij
'''
# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
 
page = 3
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
try:
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    # print content
    pattern = re.compile(r'<div class=\"author clearfix\">[\s\S]*?<a href.*? title=\"(.*?)\"',re.S)
    items = re.findall(pattern,content)
    # print items
    for item in items:
        print item
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason