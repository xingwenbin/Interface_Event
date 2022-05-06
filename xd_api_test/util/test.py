import unittest
from xd_api_test.util.request_util import RequestUtil
import json
from xd_api_test.util.config import headers ,host ,projectID

class SaveWithUser(unittest.TestCase):
    '''
    新增修改网格用户
    '''
    def test_saveWithUser(self):

        request = RequestUtil()
        url = host +"/gridauth/grid/saveWithUser"
        projectId = projectID
        data = {"gridName":"测试","bussType":"water","centerLevel":0,"gridDesc":"测试备注","gridParent":"","gridSort":0,"latitude":0,"longitude":0,"userList":[{"projectId":projectId,"sysCode":"water","userIds":"1293728767227408385"},{"projectId":projectId,"sysCode":"water","userIds":"1379614107731165186"},{"projectId":projectID,"sysCode":"water","userIds":"1483681551425028098"}],"gridId":"4ddc0c54908e11eca65ffa163e85f750","projectId":projectId}
        # response = request.request(url, 'post', headers=headers, param=data, content_type = 'application/json')
        data = {
          "gridName": "3",
          "bussType": "air4",
          "centerLevel": 0,
          "gridDesc": "",
          "gridParent": "7fcd719a908e11eca65ffa163e85f750",
          "gridSort": 0,
          "latitude": 0,
          "longitude": 0,
          "userList": [
            {
              "projectId": projectId,
              "sysCode": "air4",
              "userIds": "1302782259254726659"
            }
          ],
          "projectId": projectId
        }
        response = request.request(url,'post', headers=headers,param=data,content_type='application/json')

        #print(headers)
        '''
        {
  "gridName": "1",
  "bussType": "air4",
  "centerLevel": 0,
  "gridDesc": "",
  "gridParent": "7fcd719a908e11eca65ffa163e85f750",
  "gridSort": 0,
  "latitude": 0,
  "longitude": 0,
  "userList": [
    {
      "projectId": "1209302080142258176",
      "sysCode": "air4",
      "userIds": "1302782259254726659"
    }
  ],
  "projectId": "1209302080142258176"
}
        '''

        #print(response['data']['records'][0]['mobile'])

        print(url)
        print(data)
        print(response)

        #self.assertEqual(response['data'],"4ddc0c54908e11eca65ffa163e85f750")
        #self.assertEqual(response['data']['records'][0]['mobile'],'18511248407')
        #
        #self.assertTrue(len(response['data']) > 0, "分类列表为空")


if __name__ == '__main__':
     unittest.main(verbosity=2)