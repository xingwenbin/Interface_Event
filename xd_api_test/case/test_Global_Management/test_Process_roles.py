# _*_ coding: utf-8 _*_
"""
Time:     2022-03-28 14:07
Author:   Xing Wen Bin
Version:  V 0.1
File:     test_Process_roles.py
Describe: 全局管理中得流程角色管理, Github link: https://github.com/Deeachain/GraphEmbeddings
"""
import unittest
from xd_api_test.util.config import *
from xd_api_test.util.request_util import RequestUtil
import random
class Process_roles(unittest.TestCase):

    ''' 流程角色管理 '''

    def test_1_Add_Process(self):

        ''' 添加角色 '''
        url = 'http://srv-newgrid-gateway---integrated.jiahuayun-huanbao-dev.rocktl.com/grid/v1/gridauth/gridrole/save'
        roleCode = random.randint(10000,99999)
        data = {
              "roleName": roleName,
              "roleDesc": "这是备注",
              "roleCode": roleCode,
              "user": []
        }
        print(data)
        request = RequestUtil()
        response = request.request(url,'post',headers=headers,param=data,content_type='application/json')
        print(response)
        self.assertEqual(response['msg'], "新增成功")

    # def test_4_Add_Process(self):
    #
    #     ''' 新增/编辑：角色编码已存在 '''
    #     url = 'http://srv-newgrid-gateway---integrated.jiahuayun-huanbao-dev.rocktl.com/grid/v1/gridauth/gridrole/save'
    #     data = {
    #           "roleName": roleName,
    #           "roleDesc": "这是备注",
    #           "roleCode": 'b57571739e5411ea8efc002219996ac5',
    #           "user": []
    #     }
    #     print(data)
    #     request = RequestUtil()
    #     response = request.request(url,'post',headers=headers,param=data,content_type='application/json')
    #     print(response)
    #     self.assertEqual(response['message'], "角色编码已存在")
    def test_2_Updat_Process(self):

        ''' 编辑角色'''
        url = 'http://srv-newgrid-gateway---integrated.jiahuayun-huanbao-dev.rocktl.com/grid/v1/gridauth/gridrole/save'
        RoleId = Process_roles.get_RoleId()
        roleCode = Process_roles.get_RoleCode()
        data = {
              "deleteFlag": 0,
              "roleCode": roleCode,
              "roleDesc": "这是新备注进行修改",
              "roleId": RoleId,
              "roleName": roleName
        }
        print(data)
        request = RequestUtil()
        response = request.request(url, 'post', headers=headers, param=data, content_type='application/json')
        self.assertEqual(response['msg'], "新增成功")



    def test_3_Delete_Process(self):

        ''' 删除角色 '''
        RoleId = Process_roles.get_RoleId()

        print(RoleId)

        url = 'http://srv-newgrid-gateway---integrated.jiahuayun-huanbao-dev.rocktl.com/grid/v1/gridauth/gridrole/delete'
        data ={
            'roleId':RoleId
           ,'projectId': '1209302080142258176'
        }
        request = RequestUtil()
        print(data)
        response = request.request(url, 'get', headers=headers, param=data, content_type='application/json')
        self.assertEqual(response['msg'], "查询成功")

    def get_RoleId():

        ''' 获取roleId'''

        url = 'http://srv-newgrid-gateway---integrated.jiahuayun-huanbao-dev.rocktl.com/grid/v1/gridauth/gridrole/list'
        request = RequestUtil()
        response = request.request(url, 'get', headers=headers, content_type='application/json')
        for i in response['data']:
            if i['roleName'] == roleName:
                return i['roleId']

    def get_RoleCode():
        ''' 获取roleCode'''
        url = 'http://srv-newgrid-gateway---integrated.jiahuayun-huanbao-dev.rocktl.com/grid/v1/gridauth/gridrole/list'
        request = RequestUtil()
        response = request.request(url, 'get', headers=headers, content_type='application/json')
        for i in response['data']:
            if i['roleName'] == roleName:
                return i['roleCode']
