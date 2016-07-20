# import urllib 
# import urllib2 
# url = 'http://www.pythontab.com' 
# values = {'name' : 'Michael Foord', 
#           'location' : 'pythontab', 
#           'language' : 'Python' } 
# data = urllib.urlencode(values) 
# req = urllib2.Request(url, data) 
# response = urllib2.urlopen(req) 
# the_page = response.read()
# print the_page

# import urllib2
# req = urllib2.Request("http://www.baidu.com")
# fd=urllib2.urlopen(req)
# data = fd.read()
# print data

import urllib2
req = urllib2.Request("http://www.google.com")
fd=urllib2.urlopen(req)
data = fd.read()
print data

