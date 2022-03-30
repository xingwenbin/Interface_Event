# coding = utf-8

import unittest
from xd_api_test.util.request_util import RequestUtil
from xd_api_test.util.config import headers
import json

# host = "http://srv-newgrid-event---integrated.jiahuayun-huanbao-dev.rocktl.com"
headers = headers
class Event(unittest.TestCase):

    def test_Event(self):
        ''' 事件中心业务：查询督察事件'''
        """
        查询督察事件
        """

        # host = "https://srv-newgrid-event---integrated.jiahuayun-huanbao-dev.rocktl.com"
        request = RequestUtil()
        url = 'http://srv-newgrid-gateway---integrated.jiahuayun-huanbao-dev.rocktl.com/grid/v1/gridevent/event/supervision/info'
        # heades = {'Authorization-sys': 'Bearer eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJVU0VSIiwiZGF0YSI6eyJyZWdpb25JZCI6NTAwMTE3MDAwLCJyZWdpb25UeXBlIjoiRElTVFJJQ1QiLCJjaWQiOjEyMDkzMDIwODAxNDIyNTgxNzYsImxvZ2luSWQiOjE0MiwibG9naW5OYW1lIjoiMTg2MzYxODE3NDgiLCJyb2xlSWRzIjpbMTM2NzA0MTE5NzkxMDUyMzkxMV0sImlzQWRtaW4iOnRydWUsImlzU3VwZXJVc2VyIjp0cnVlLCJpc1JrVXNlciI6dHJ1ZSwic3lzQ29kZSI6ImV2ZW50Iiwic3lzSWQiOjEzODQzOTEzMjgwNTg1NDgyMjUsInByb3h5IjpudWxsLCJzdWIiOm51bGx9LCJpc3MiOiJSb2Nrb250cm9sLXVuaWZpZWQiLCJleHAiOjE2NDc5MzQwMTQsImlhdCI6MTY0NzkzMDQxNCwianRpIjoiMTg2MzYxODE3NDgifQ.b3GX4iut2Q0ZhMb9syS-7lr0Qm3TLw68geMfldmQv2tKiM9dNBW4Qj1EJM1P5RR_yj_IH2Fp1L8pwbfFA8G39A'}
        data = {"eventId": "7bbf6179a10311eca65ffa163e85f750"}
        response = request.request(url, 'get', param=data, headers=headers)
        # print(response['msg'] +'**********')
        self.assertEqual(response['msg'], "查询成功")


    def test_SourcesEvent(self):
        ''' 查询事件污染原因 '''
        '''
        查询事件污染原因
        :return:
        '''

        url = 'https://srv-newgrid-event---integrated.jiahuayun-huanbao-dev.rocktl.com/event/pollutionCause'
        # heades = {'Authorization-sys': 'Bearer eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJVU0VSIiwiZGF0YSI6eyJyZWdpb25JZCI6NTAwMTE3MDAwLCJyZWdpb25UeXBlIjoiRElTVFJJQ1QiLCJjaWQiOjEyMDkzMDIwODAxNDIyNTgxNzYsImxvZ2luSWQiOjE0MiwibG9naW5OYW1lIjoiMTg2MzYxODE3NDgiLCJyb2xlSWRzIjpbMTM2NzA0MTE5NzkxMDUyMzkxMV0sImlzQWRtaW4iOnRydWUsImlzU3VwZXJVc2VyIjp0cnVlLCJpc1JrVXNlciI6dHJ1ZSwic3lzQ29kZSI6ImV2ZW50Iiwic3lzSWQiOjEzODQzOTEzMjgwNTg1NDgyMjUsInByb3h5IjpudWxsLCJzdWIiOm51bGx9LCJpc3MiOiJSb2Nrb250cm9sLXVuaWZpZWQiLCJleHAiOjE2NDc5MzAyODYsImlhdCI6MTY0NzkyNjY4NiwianRpIjoiMTg2MzYxODE3NDgifQ.Ek5qUfAR83yGoVpEU1NKyx5na9z_UHZKSt8RWzR2yjDShSXDD_qQr9obqk96s28zIScaDIkCO2ZwNFUgeJsRcQ'}
        data = {"eventId": "7bbf6179a10311eca65ffa163e85f750"}
        request = RequestUtil()
        response = request.request(url, 'get', param=data,headers=headers)
        self.assertEqual(response['msg'], "查询成功")

    def test_EportEvent(self):
        ''' 上报人查询事件 '''
        '''
        上报人查询事件
        :return:
        '''
        url = 'http://srv-newgrid-gateway---integrated.jiahuayun-huanbao-dev.rocktl.com/grid/v1/gridbusiness/eventAir/pageEventsPost'
        # heades = {'Authorization-sys': 'Bearer eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJVU0VSIiwiZGF0YSI6eyJyZWdpb25JZCI6NTAwMTE3MDAwLCJyZWdpb25UeXBlIjoiRElTVFJJQ1QiLCJjaWQiOjEyMDkzMDIwODAxNDIyNTgxNzYsImxvZ2luSWQiOjE0MiwibG9naW5OYW1lIjoiMTg2MzYxODE3NDgiLCJyb2xlSWRzIjpbMTM2NzA0MTE5NzkxMDUyMzkxMV0sImlzQWRtaW4iOnRydWUsImlzU3VwZXJVc2VyIjp0cnVlLCJpc1JrVXNlciI6dHJ1ZSwic3lzQ29kZSI6ImV2ZW50Iiwic3lzSWQiOjEzODQzOTEzMjgwNTg1NDgyMjUsInByb3h5IjpudWxsLCJzdWIiOm51bGx9LCJpc3MiOiJSb2Nrb250cm9sLXVuaWZpZWQiLCJleHAiOjE2NDc5MzAyODYsImlhdCI6MTY0NzkyNjY4NiwianRpIjoiMTg2MzYxODE3NDgifQ.Ek5qUfAR83yGoVpEU1NKyx5na9z_UHZKSt8RWzR2yjDShSXDD_qQr9obqk96s28zIScaDIkCO2ZwNFUgeJsRcQ'}
        data = {
              "pageNum": '1',
              "pageSize": '10',
              "useGridAuth": 'true',
              "sysCode": "water",
              "eventType": "2",
              "queryUserId": "1483681551425028098",
              "fuzzyWord": "",
              "isSelf": '0',
              "isCollect": 'false',
              "all-event-to-center": "0",
              "all-event-list": "0",
              "startTime": "1646815091344",
              "endTime": "1647419891344",
              "isSelfFavorite": '0',
              "userId": "1483681551425028098",
              "preAuditState": "1",
              "projectId": "1209302080142258176"
            }
        request = RequestUtil()
        response = request.request(url, 'post',param = data,headers=headers,content_type='application/json')
        self.assertEqual(response['msg'], "新增成功")

    def test_Save_ducha_Event(self):
        ''' 保存督察意见 '''
        '''
        保存督察意见
        :return:
        '''
        url = 'http://srv-newgrid-gateway---integrated.jiahuayun-huanbao-dev.rocktl.com/grid/v1/gridbusiness/eventAir/saveSupervisionRecordAndExamine'
        # heades = {Authorization-sys
        #     'Authorization-sys': 'Bearer eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJVU0VSIiwiZGF0YSI6eyJyZWdpb25JZCI6NTAwMTE3MDAwLCJyZWdpb25UeXBlIjoiRElTVFJJQ1QiLCJjaWQiOjEyMDkzMDIwODAxNDIyNTgxNzYsImxvZ2luSWQiOjE0MiwibG9naW5OYW1lIjoiMTg2MzYxODE3NDgiLCJyb2xlSWRzIjpbMTM2NzA0MTE5NzkxMDUyMzkxMV0sImlzQWRtaW4iOnRydWUsImlzU3VwZXJVc2VyIjp0cnVlLCJpc1JrVXNlciI6dHJ1ZSwic3lzQ29kZSI6ImV2ZW50Iiwic3lzSWQiOjEzODQzOTEzMjgwNTg1NDgyMjUsInByb3h5IjpudWxsLCJzdWIiOm51bGx9LCJpc3MiOiJSb2Nrb250cm9sLXVuaWZpZWQiLCJleHAiOjE2NDc5MzAyODYsImlhdCI6MTY0NzkyNjY4NiwianRpIjoiMTg2MzYxODE3NDgifQ.Ek5qUfAR83yGoVpEU1NKyx5na9z_UHZKSt8RWzR2yjDShSXDD_qQr9obqk96s28zIScaDIkCO2ZwNFUgeJsRcQ'}
        data = {
            "checkFlag": "1",
            "objId": "",
            "remark": "督察复查通过意见",
            "eventId": "f9a92bc09a0911eca65ffa163e85f750",
            "instanceId": "00f776289ebb11eca65ffa163e85f750",
            "objName": "",
            "scoreTime": "1647333734297",
            "sysCode": "water",
            "userId": "1483681551425028098",
            "userName": "邢文斌",
            "projectId": "1209302080142258176"
        }
        request = RequestUtil()
        response = request.request(url, 'post', param=data, headers=headers, content_type='application/json')
        print(response)
        self.assertEqual(response['msg'], "新增成功")


    def test_To_Do_Event(self):
        ''' 保存督察意见 '''
        '''
        待办事件查询
        :return:
        '''

        url = 'http://srv-newgrid-gateway---integrated.jiahuayun-huanbao-dev.rocktl.com/grid/v1/gridbusiness/eventAir/pageEventsPost'
        data = {
          "pageNum": 1,
          "pageSize": 10,
          "useGridAuth": 'true',
          "sysCode": "water",
          "eventType": "2",
          "queryUserId": "",
          "dealCode": "4",
          "deviceTypeCode": "W01",
          "isSelf": 0,
          "isCollect": 'false',
          "all-event-to-center": "0",
          "all-event-list": "0",
          "startTime": "1647571106090",
          "endTime": "1648175906090",
          "isSelfFavorite": 0,
          "userId": "1483681551425028098",
          "preAuditState": "1",
          "projectId": "1209302080142258176"
        }
        request = RequestUtil()
        response = request.request(url, 'post', param=data,headers=headers,content_type='application/json')
        self.assertEqual(response['msg'], "新增成功")
    def test_Have_To_Do_Event(self):
        ''' 已办事件查询 '''
        '''
        已办事件查询
        :return:
        '''

        url = 'http://srv-newgrid-gateway---integrated.jiahuayun-huanbao-dev.rocktl.com/grid/v1/gridbusiness/eventAir/pageEventsPost'
        data = {
          "pageNum": 1,
          "pageSize": 10,
          "useGridAuth": 'true',
          "sysCode": "water",
          "eventType": "2",
          "queryUserId": "",
          "dealCode": "7",
          "deviceTypeCode": "W01",
          "isSelf": 0,
          "isCollect": 'false',
          "all-event-to-center": "0",
          "all-event-list": "0",
          "startTime": "1647571106090",
          "endTime": "1648175906090",
          "isSelfFavorite": 0,
          "userId": "1483681551425028098",
          "preAuditState": "1",
          "projectId": "1209302080142258176"
        }
        request = RequestUtil()
        response = request.request(url, 'post', param=data,headers=headers,content_type='application/json')
        self.assertEqual(response['msg'], "新增成功")
    def test_Have_To_Do_Event(self):
        ''' 事件标题事件查询 '''
        '''
        事件标题事件查询
        :return:
        '''

        url = 'http://srv-newgrid-gateway---integrated.jiahuayun-huanbao-dev.rocktl.com/grid/v1/gridbusiness/eventAir/pageEventsPost'
        data = {
          "pageNum": 1,
          "pageSize": 10,
          "useGridAuth": 'true',
          "sysCode": "water",
          "eventType": "2",
          "queryUserId": "",
          "fuzzyWord": "测试",
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
        self.assertEqual(response['msg'], "新增成功")

    def getqueryUserId():

        ''' 查询人员ID '''
        '''
        查询人员ID
        :return:
        '''

        host = 'http://srv-newgrid-gateway---integrated.jiahuayun-huanbao-dev.rocktl.com/grid/v1/sys/org/getTreeUserBySysCode'
        data = {
            'sysCode': 'water',
            'searchName': '13353431635'
        }
        request = RequestUtil()
        response = request.request(host, 'get', param=data,headers=headers)
        # print(response['data']['child'][0]['child'][0]['id'])
        return response['data']['child'][0]['child'][0]['id']

    def test_Phone_Sele_Event(self):
        ''' 上报人查询事件 '''
        url='http://srv-newgrid-gateway---integrated.jiahuayun-huanbao-dev.rocktl.com/grid/v1/gridbusiness/eventAir/pageEventsPost'
        queryUserId = Event.getqueryUserId()
        data ={
          "pageNum": 1,
          "pageSize": 10,
          "useGridAuth": 'true',
          "sysCode": "water",
          "eventType": "2",
          "queryUserId": queryUserId,
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
        self.assertEqual(response['msg'], "新增成功")
    def api_add_Event(self):
        '''  新增事件  '''
        url = 'http://srv-grid-gateway---integrated.jiahuayun-huanbao-dev.rocktl.com'
        host = url + '/grid/v1/gridbusiness/eventAir/eventReport'
        headers = {'Content-Type': 'application/json;charset=UTF-8', 'Accept': 'application/json, text/plain, */*', 'Authorization-sys' : 'Bearer eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJVU0VSIiwiZGF0YSI6eyJyZWdpb25JZCI6NTAwMTE3MDAwLCJyZWdpb25UeXBlIjoiRElTVFJJQ1QiLCJjaWQiOjEyMDkzMDIwODAxNDIyNTgxNzYsImxvZ2luSWQiOjE0ODM2ODE1NTE0MjUwMjgwOTgsImxvZ2luTmFtZSI6IjEzMzUzNDMxNjM1Iiwicm9sZUlkcyI6WzEzNjcwNDExOTc5MTA1MjM5MTEsMTQyNzQ2ODU0MTQzMjYwNjcyMV0sImlzQWRtaW4iOmZhbHNlLCJpc1N1cGVyVXNlciI6ZmFsc2UsImlzUmtVc2VyIjpmYWxzZSwic3lzQ29kZSI6ImV2ZW50Iiwic3lzSWQiOjEzODQzOTEzMjgwNTg1NDgyMjUsInByb3h5IjpudWxsLCJzdWIiOm51bGx9LCJpc3MiOiJSb2Nrb250cm9sLXVuaWZpZWQiLCJleHAiOjE2NDgwMjA4MTQsImlhdCI6MTY0ODAxNzIxNCwianRpIjoiMTMzNTM0MzE2MzUifQ.D16ute0ApVfnAPauPiwQmAqfZ7rA2OJL3nq8ig0YRPlegzcEAuYvJhSoRBMaO9NXUIVL8qhBiqEFbO2FMF6IyA'}
        data = {
              "gridId": "-1",
              "title": "测试事件",
              "eventType": "2",
              "eventSource": "222",
              "pcauses": [
                "00000004"
              ],
              "referName": "",
              "reportType": "2",
              "bussType": "water",
              "sysCode": "water",
              "address": "山西省太原市小店区坞城街道南中环街246号光信·国信嘉园",
              "longitude": 112.57376,
              "latitude": 37.7956,
              "imagePaths": "",
              "deviceTypeName": "",
              "deviceName": "",
              "pollutionTypeName": "",
              "pollutionName": "",
              "encPathList": [],
              "userId": '1483681551425028098',
              "projectId": "1209302080142258176"
            }
        print(host)
        print(headers)
        print(data)
        request = RequestUtil()
        # re = requests.post(url=host,headers=headers,json=data).json()
        # re = requests.post(url=host,)
        response =request.request(host,'post',headers=headers,param=data)
        self.assertEqual(response['msg'], "新增成功")
if __name__ == '__main__':
     unittest.main(verbosity=2)
   # DeleteEvent.deleteEvent()



