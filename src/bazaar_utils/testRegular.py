'''
Created on Apr 21, 2016

@author: cuij
'''
# -*- coding:utf-8 -*-
import re

pattern = re.compile(r'<div class="author clearfix">[\s\S]*?<a href.*? title="(.*?)">[\s\S]*?<div class="content">\r\n\r\n(.*)[\s\S]<!--.*?-->[\s\S]*?<i class="number">(.*)</i>[\s\S]*<i class="number">(.*)</i>.*[\s\S]*</span>')
print " the pattern is ",pattern
print re.findall(pattern,'one1two2three3four4')
