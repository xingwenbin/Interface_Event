# _*_ coding: utf-8 _*_
"""
Time:     2022-03-28 16:45
Author:   Xing Wen Bin
Version:  V 0.1
File:     test_In_Management.py
Describe: 全局管理中的接口管理，其中包含新增接口、查看、删除、按项目类型、地址key查询等方法, Github link: https://github.com/Deeachain/GraphEmbeddings
"""
import unittest
from xd_api_test.util.config import *
from xd_api_test.util.request_util import RequestUtil
class Interface_Management(unittest.TestCase):
    ''' 接口管理相关业务'''
    def test_1_Add_Interface(self):
        '''新增接口'''
        url = 'http://srv-newgrid-gateway---integrated.jiahuayun-huanbao-dev.rocktl.com/grid/v1/gridauth/pinter'
        data = {
          "projectId": "0",
          "uri": "www.baidu.com",
          "uriKey": "iam_test",
          "uriType": "1",
          "methodType": "GET",
          "remark": "这里是描述",
          "projectName": "通用项目"
        }
        request = RequestUtil()
        response = request.request(url,'post', headers=headers,param=data,content_type='application/json')
        print(response)
        self.assertEqual(response['msg'], "新增成功")
        print(response['data'])
        return response['data']

    def test_2_Updata_Interface(self):
        ''' 查看接口 '''

        interId = Interface_Management.test_1_Add_Interface(self)
        # print(interId)
        url = 'http://srv-newgrid-gateway---integrated.jiahuayun-huanbao-dev.rocktl.com/grid/v1/gridauth/pinter/'+ interId
        request = RequestUtil()
        response = request.request(url,'get', headers=headers)
        # print(response)
        self.assertEqual(response['msg'], "查询成功")
    def test_3_Delete_Interface(self):
        ''' 删除接口 '''

        interId = Interface_Management.test_1_Add_Interface(self)
        # print(interId)
        url = 'http://srv-newgrid-gateway---integrated.jiahuayun-huanbao-dev.rocktl.com/grid/v1/gridauth/pinter/delete/'+ interId
        request = RequestUtil()
        response = request.request(url,'get', headers=headers)
        # print(response)
        self.assertEqual(response['msg'], "查询成功")

    def test_4_Select_Project(self):
        ''' 所属地址key查询'''
        url = 'http://srv-newgrid-gateway---integrated.jiahuayun-huanbao-dev.rocktl.com/grid/v1/gridauth/pinter/page'
        data ={
            'pageSize': '20',
            'pageNum': '1',
            'total': '60',
            'key':'dept_byproject_inter',
            'projectId': ''
        }
        request = RequestUtil()
        re = request.request(url,'get', headers=headers,param=data,content_type='application/json')
        print(re)
        self.assertEqual(re['msg'], "查询成功")

    def test_4_Select_Project(self):

        ''' 所属所属项目查询'''
        url = 'http://srv-newgrid-gateway---integrated.jiahuayun-huanbao-dev.rocktl.com/grid/v1/gridauth/pinter/page'
        data ={
            'pageSize': '20',
            'pageNum': '1',
            'total': '0',
            'key':'',
            'projectId': '0'
        }
        request = RequestUtil()
        re = request.request(url,'get', headers=headers,param=data,content_type='application/json')
        print(re)
        self.assertEqual(re['msg'], "查询成功")