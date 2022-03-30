# _*_ coding: utf-8 _*_
"""
Time:     2022-03-25 9:19
Author:   Xing Wen Bin
Version:  V 0.1
File:     test.py
Describe: Write during the internship at Hikvison, Github link: https://github.com/Deeachain/GraphEmbeddings
"""

from xd_api_test.util.config import headers
from xd_api_test.util.request_util import RequestUtil
class test():
    def getqueryUserId():

        host = 'http://srv-newgrid-gateway---integrated.jiahuayun-huanbao-dev.rocktl.com/grid/v1/sys/org/getTreeUserBySysCode?sysCode=water&searchName=13353431635'
        data = {
            'sysCode': 'water',
            'searchName': '13353431635'
        }
        request = RequestUtil()
        response = request.request(host, 'get', headers=headers)
        print(response)
        print(type(response['data']['child'][0]['child'][0]['id']))
        # print(response['data']['child']['0']['child']['0']['id'])
        return response['data']['child'][0]['child'][0]['id']
    def test_Phone_Sele_Event():
        url='http://srv-newgrid-gateway---integrated.jiahuayun-huanbao-dev.rocktl.com/grid/v1/gridbusiness/eventAir/pageEventsPost'
        rs = test.getqueryUserId()
        print(rs +'********' )
        data ={
          "pageNum": 1,
          "pageSize": 10,
          "useGridAuth": 'true',
          "sysCode": "water",
          "eventType": "2",
          "queryUserId": f'{rs}',
          "fuzzyWord": "",
          "isSelf": 0,
          "isCollect": 'false',
          "all-event-to-center": "0",
          "all-event-list": "0",
          "startTime": "1647571999395",
          "endTime": "1648176799395",
          "isSelfFavorite": 0,
          "userId": "1483681551425028098",
          "preAuditState": "1",
          "projectId": "1209302080142258176"
        }

        request = RequestUtil()
        response = request.request(url, 'post', param=data,headers=headers,content_type='application/json')
        print(response)
if __name__ == '__main__':
    test.test_Phone_Sele_Event()