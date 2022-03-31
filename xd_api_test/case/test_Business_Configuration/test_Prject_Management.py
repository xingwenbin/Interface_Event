# _*_ coding: utf-8 _*_
"""
Time:     2022-03-29 11:05
Author:   Xing Wen Bin
Version:  V 0.1
File:     test_Prject_Management.py
Describe: Write during the internship at Hikvison, Github link: https://github.com/Deeachain/GraphEmbeddings
"""
import unittest
from xd_api_test.util.config import *
from xd_api_test.util.request_util import RequestUtil

class Project_Management(unittest.TestCase):



    ''' 项目管理'''

    def test_1_Set_up_the(self):
        ''' 设置业务：开启 '''
        url = 'http://srv-newgrid-gateway---integrated.jiahuayun-huanbao-dev.rocktl.com/grid/v1/gridauth/pconfig/updateIsStartFlow'
        data = {
            'configValue': '1',
            'projectId': '1209302080142258176'
        }
        request =RequestUtil()
        re = request.request(url,'post',headers=headers,param=data,content_type='application/json')
        print(re)
        self.assertEqual(re['msg'], "新增成功")

    def test_2_Set_down_the(self):
        ''' 设置业务：关闭  '''
        url = 'http://srv-newgrid-gateway---integrated.jiahuayun-huanbao-dev.rocktl.com/grid/v1/gridauth/pconfig/updateIsStartFlow'
        data = {
            'configValue': '0',
            'projectId': '1209302080142258176'
        }
        request = RequestUtil()
        re = request.request(url, 'post', headers=headers, param=data, content_type='application/json')
        print(re)
        self.assertEqual(re['msg'], "新增成功")

