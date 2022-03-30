# _*_ coding: utf-8 _*_
"""
Time:     2022-03-16 11:34
Author:   Xing Wen Bin
Version:  V 0.1
File:     DelEvent.py
Describe: Write during the internship at Hikvison, Github link: https://github.com/Deeachain/GraphEmbeddings
"""
import requests
import response
import re as r
from xd_api_test.util.request_util import RequestUtil

class APIdelEvent():
    '''

    '''
    # url = 'http://srv-grid-gateway---integrated.jiahuayun-huanbao-dev.rocktl.com'
    # def setUp(self):
    #     self.url = 'http://srv-grid-gateway---integrated.jiahuayun-huanbao-dev.rocktl.com'
    #     self.cookesValue = ''
    #     self.userID = '1483681551425028098'
    #     self.projectID = '1209302080142258176'
    #     self.replaceGridId = '3f05eb59909011eca65ffa163e85f750'

    def api_add_Event():
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
        re =request.request(host,'post',headers=headers,param=data)
        print(re)
        return re['data']

    def api_send_Event():
        url = 'http://srv-grid-gateway---integrated.jiahuayun-huanbao-dev.rocktl.com'
        host = url + '/grid/v1/gridbusiness/wk/doWork'
        headers = {'Accept': 'application/json, text/plain, */*',
                   'Authorization-sys':'Bearer eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJVU0VSIiwiZGF0YSI6eyJyZWdpb25JZCI6NTAwMTE3MDAwLCJyZWdpb25UeXBlIjoiRElTVFJJQ1QiLCJjaWQiOjEyMDkzMDIwODAxNDIyNTgxNzYsImxvZ2luSWQiOjE0ODM2ODE1NTE0MjUwMjgwOTgsImxvZ2luTmFtZSI6IjEzMzUzNDMxNjM1Iiwicm9sZUlkcyI6WzEzNjcwNDExOTc5MTA1MjM5MTEsMTQyNzQ2ODU0MTQzMjYwNjcyMV0sImlzQWRtaW4iOmZhbHNlLCJpc1N1cGVyVXNlciI6ZmFsc2UsImlzUmtVc2VyIjpmYWxzZSwic3lzQ29kZSI6ImV2ZW50Iiwic3lzSWQiOjEzODQzOTEzMjgwNTg1NDgyMjUsInByb3h5IjpudWxsLCJzdWIiOm51bGx9LCJpc3MiOiJSb2Nrb250cm9sLXVuaWZpZWQiLCJleHAiOjE2NDgwMjA4MTQsImlhdCI6MTY0ODAxNzIxNCwianRpIjoiMTMzNTM0MzE2MzUifQ.D16ute0ApVfnAPauPiwQmAqfZ7rA2OJL3nq8ig0YRPlegzcEAuYvJhSoRBMaO9NXUIVL8qhBiqEFbO2FMF6IyA'}

        eventId = APIdelEvent.api_add_Event()
        print(eventId)
        operId = APIdelEvent.get_operid()
        print(operId)

        data = {
              "eventId":eventId,
              "latitude": 0,
              "longitude": 0,
              "eventTitle": "${eventTitle}",
              "gridId": "-1",
              "operDesc": "派遣",
              "statusCode": "0",
              "operId": operId,
              "selectOperMode": "5",
              "replaceGridFlag": "1",
              "replaceGridId": "${replaceGridId}",
              "suggest": "测试事件",
              "imagePaths": ""
        }
        re = requests.post(host,param=data, headers=headers).json()
        print(re)

    def get_operid():
        url = 'http://srv-grid-gateway---integrated.jiahuayun-huanbao-dev.rocktl.com'

        host = url + '/grid/v1/gridbusiness/eventAir/eventInfo'
        headers = {'Accept':'application/json, text/plain, */*',
                   'Authorization-sys':'Bearer eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJVU0VSIiwiZGF0YSI6eyJyZWdpb25JZCI6NTAwMTE3MDAwLCJyZWdpb25UeXBlIjoiRElTVFJJQ1QiLCJjaWQiOjEyMDkzMDIwODAxNDIyNTgxNzYsImxvZ2luSWQiOjE0ODM2ODE1NTE0MjUwMjgwOTgsImxvZ2luTmFtZSI6IjEzMzUzNDMxNjM1Iiwicm9sZUlkcyI6WzEzNjcwNDExOTc5MTA1MjM5MTEsMTQyNzQ2ODU0MTQzMjYwNjcyMV0sImlzQWRtaW4iOmZhbHNlLCJpc1N1cGVyVXNlciI6ZmFsc2UsImlzUmtVc2VyIjpmYWxzZSwic3lzQ29kZSI6ImV2ZW50Iiwic3lzSWQiOjEzODQzOTEzMjgwNTg1NDgyMjUsInByb3h5IjpudWxsLCJzdWIiOm51bGx9LCJpc3MiOiJSb2Nrb250cm9sLXVuaWZpZWQiLCJleHAiOjE2NDgwMjA4MTQsImlhdCI6MTY0ODAxNzIxNCwianRpIjoiMTMzNTM0MzE2MzUifQ.D16ute0ApVfnAPauPiwQmAqfZ7rA2OJL3nq8ig0YRPlegzcEAuYvJhSoRBMaO9NXUIVL8qhBiqEFbO2FMF6IyA'}
        data ={
            'eventId':APIdelEvent.api_add_Event(),
            'userId' : '1483681551425028098'
        }
        res = requests.get(host,params=data,headers=headers).json()
        operId = res['data']['operId']

        # print(res['data']['operId'])
        return operId
        # print(type(res))
        # print(res.get('operid'))
        # print(res = r.findall('"operId":(.+?),"param":"',res))
        # print(re['data'])



if __name__ == '__main__':
    # APIdelEvent.api_send_Event()
    APIdelEvent.api_add_Event()