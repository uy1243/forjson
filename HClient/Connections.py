'''
Created on Jan 8, 2018

@author: yu
'''
import sys
import requests
import json
import unittest
#encoding: utf-8
class Connnection2lvge(unittest.TestCase):
    
    #def __init__(self):
        #super(Connnection2lvge, self).__init__()
    def mkHeaders_login(self):
        s = requests.Session()
        headers = {
                'Accept':'application/json, text/javascript, */*; q=0.01',
                'Accept-Encoding':'gzip, deflate',
                'Accept-Language':'en-US,en;q=0.9',
                'Connection':'keep-alive',
                'Content-Length':'15',
                'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
                'Host':'www.lvgew.com',
                'Origin':'http://www.lvgew.com',
                'Referer':'http://www.lvgew.com/purview/user/toTopNav',
                'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
                'X-Requested-With':'XMLHttpRequest'}

        param2lvge = {'name': '\u6cb3\u5357\u65c5\u9e3d\u79d1\u6280\u6709\u9650\u516c\u53f8', 'password': '12345678'}
        r = s.post('http://www.lvgew.com/purview/user/login', params=param2lvge, headers=headers, timeout=10)
        res2 = s.post('http://www.lvgew.com/purview/user/toHome')
        print 'hi'
        print r.text
        #return r.json()
    def runTest(self):
        self.mkHeaders_login()