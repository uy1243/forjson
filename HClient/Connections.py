# encoding: utf-8
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
                'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
                'X-Requested-With':'XMLHttpRequest'}

        param2lvge = {'name': '河南旅鸽科技有限公司','password': '12345678'}
        r = s.post('http://www.lvgew.com/purview/user/login', params=param2lvge, headers=headers, timeout=6)
        #r = requests.post('http://www.lvgew.com/purview/user/toLogin', params=param2lvge, headers=headers, timeout=6)
        #res2 = s.post('http://www.lvgew.com/purview/user/toHome')
        
        toadd = {'name': '','pageSize':'20','pageIndex':'1'}
        res2 = s.post('http://www.lvgew.com/basic/brand/query', params=toadd, headers=headers, timeout=6)
        print res2.content
        res=json.dumps(res2.content)
        imgloc='http://www.lvgew.com/basic/brand/getImage?entityID=132&r=0.8790690929159222&type=2'
        #print res
        with open('./1.html', 'wb') as f:
            f.write(res2.content)
        #return r.json()
    def runTest(self):
        self.mkHeaders_login()