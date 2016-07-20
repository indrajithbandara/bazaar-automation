'''
Created on Jun 13, 2016

@author: cuij
'''
import httplib, urllib

host = 'http://baz-jenkins/'
url = '/view/devops/job/automate-deploy-zookeeper/configure'

values = {
  'val1' : '123',
  'val2' : 'abc',
}

headers = {
    'User-Agent': 'python',
    'Content-Type': 'application/x-www-form-urlencoded',
}

values = urllib.urlencode(values)

conn = httplib.HTTPSConnection(host)
conn.request("POST", url, values, headers)
response = conn.getresponse()

data = response.read()

print 'Response: ', response.status, response.reason
print 'Data:'
print data