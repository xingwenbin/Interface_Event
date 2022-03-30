# _*_ coding: utf-8 _*_
"""
Time:     2022-03-28 15:27
Author:   Xing Wen Bin
Version:  V 0.1
File:     test_Report_Source.py
Describe: 全局管理中上报来源管理，包含新增、修改、删除, Github link: https://github.com/Deeachain/GraphEmbeddings
"""

from xd_api_test.util.config import *
from xd_api_test.util.request_util import RequestUtil
import unittest
import random

class Report_Soirce(unittest.TestCase):

    ''' 上报来源管理 '''

    def test_1_Add_Source(self):

        ''' 新增上报来源 '''
        sourceCode = random.randint(1000000,9000000)
        url = 'http://srv-newgrid-gateway---integrated.jiahuayun-huanbao-dev.rocktl.com/grid/v1/gridevent/source/add'
        data ={
          "sourceCode": sourceCode,
          "sourceName": "测试" + str(sourceCode)
        }
        request = RequestUtil()
        re = request.request(url, 'post', headers=headers, param=data, content_type='application/json')
        print(re)
        self.assertEqual(re['msg'], "新增成功")


    def test_2_Updata_Source(self):

        ''' 编辑上报来源 '''
        url = 'http://srv-newgrid-gateway---integrated.jiahuayun-huanbao-dev.rocktl.com/grid/v1/gridevent/source/update'
        sourceCode = random.randint(1000000, 9000000)
        data = {
          "sourceCode": "8839041",
          "sourceName": "上报来源编辑测试：" + str(sourceCode)
        }
        request = RequestUtil()
        re = request.request(url, 'post', headers=headers, param=data, content_type='application/json')
        print(re)
        self.assertEqual(re['msg'], "新增成功")


    def test_3_Delete_Source(self):

        ''' 删除上报来源管理 '''
        url = 'http://srv-newgrid-gateway---integrated.jiahuayun-huanbao-dev.rocktl.com/grid/v1/gridevent/source/delete'
        sourceCode = Report_Soirce.get_SourceCode()

        data ={'sourceCode': sourceCode}
        request = RequestUtil()
        re = request.request(url, 'post', headers=headers, param=data)
        self.assertEqual(re['msg'], "新增成功")

    def test_4_restore_Source(self):
        ''' 回收站恢复上报来源'''
        url = 'http://srv-newgrid-gateway---integrated.jiahuayun-huanbao-dev.rocktl.com/grid/v1/gridevent/source/project/recover'
        sourceCode = Report_Soirce.get_SourceCode()
        data ={'sourceCode': sourceCode}
        request = RequestUtil()
        re = request.request(url, 'post', headers=headers, param=data)
        self.assertEqual(re['msg'], "新增成功")
    def test_5_Sleect_Source(self):
        ''' 上报来源编码查询 '''
        url = 'http://srv-newgrid-gateway---integrated.jiahuayun-huanbao-dev.rocktl.com/grid/v1/gridbusiness/base/getEventSourceList'
        sourceCode = Report_Soirce.get_SourceCode()
        data = {
            'content': sourceCode
        }
        request = RequestUtil()
        re = request.request(url, 'get', headers=headers, param=data)
        self.assertEqual(re['msg'], "查询成功")

    def get_SourceCode():
        url = 'http://srv-newgrid-gateway---integrated.jiahuayun-huanbao-dev.rocktl.com/grid/v1/gridbusiness/base/getEventSourceList'
        data ={
            'content':''
        }
        request = RequestUtil()
        re = request.request(url,'get',headers= headers, param=data)
        for i in re['data']:
            if i['sourceName'] == sourceName:
                # print(i)
                # print(i['sourceCode'])
                return i['sourceCode']
