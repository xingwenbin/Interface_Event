# _*_ coding: utf-8 _*_
"""
Time:     2022-03-25 16:13
Author:   Xing Wen Bin
Version:  V 0.1
File:     test_Event_List.py
Describe: 热力地图事件模块，包含事件列表、我的待办等包含其中的各字段查询, Github link: https://github.com/Deeachain/GraphEmbeddings
"""
from xd_api_test.util.config import *
from xd_api_test.util.request_util import RequestUtil
import unittest
# class EventList():
#     pass

class My_to_do(unittest.TestCase):
    ''' 事件列表 '''

    def test_statMyTaskSite(self):
        ''' 事件列表查询 '''
        url ='http://srv-newgrid-gateway---integrated.jiahuayun-huanbao-dev.rocktl.com/grid/v1/gridbusiness/event/pageEventsPost'
        print(url)
        data ={
          "dealCode": "",
          "sysCode": "",
          "reportType": "",
          "useGridAuth": 'true',
          "userId": "1483681551425028098",
          "pageNum": 1,
          "pageSize": 20,
          "startTime": 1646027760000,
          "endTime": 1648446960000,
          "projectId": "1209302080142258176"
        }
        request = RequestUtil()
        response = request.request(url, 'post', headers=headers, param=data, content_type='application/json')
        # response['msg']
        print(response)
        # self.assertEqual(response['msg'], "新增成功")




if __name__ == '__main__':
    unittest.main(verbosity=2)