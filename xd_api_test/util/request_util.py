import requests


"""
Http工具类封装
"""

class RequestUtil:

    def __init__(self):
        pass

    def request(self, url, method, headers=None, param=None, content_type=None):
        """
        通用请求工具类
        :param url:
        :param method:
        :param headers:
        :param param:
        :param content_type:
        :return:
        """
        try:
            if method == 'get':
                result = requests.get(url=url, params=param, headers=headers).json()
                return result
            elif method == 'post':
                if content_type == 'application/json':
                    result = requests.post(url=url, json=param, headers=headers).json()
                    return result
                else:
                    result = requests.post(url=url, data=param, headers=headers).json()
                    return result
            else:
                print("http method not allowed")


        except Exception as e:
            print("http请求报错:{0}".format(e))


if __name__ == '__main__':
    # url = "https://api.xdclass.net/pub/api/v1/web/all_category"
    # r = RequestUtil()
    # result = r.request(url, 'get')
    # print(result)

    url = "http://srv-newgrid-gateway---integrated.jiahuayun-huanbao-dev.rocktl.com/grid/v1/gridevent/event/supervision/info"
    r = RequestUtil()
    heades = {'Authorization-sys': 'Bearer eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJVU0VSIiwiZGF0YSI6eyJyZWdpb25JZCI6NTAwMTE3MDAwLCJyZWdpb25UeXBlIjoiRElTVFJJQ1QiLCJjaWQiOjEyMDkzMDIwODAxNDIyNTgxNzYsImxvZ2luSWQiOjE0MiwibG9naW5OYW1lIjoiMTg2MzYxODE3NDgiLCJyb2xlSWRzIjpbMTM2NzA0MTE5NzkxMDUyMzkxMV0sImlzQWRtaW4iOnRydWUsImlzU3VwZXJVc2VyIjp0cnVlLCJpc1JrVXNlciI6dHJ1ZSwic3lzQ29kZSI6ImV2ZW50Iiwic3lzSWQiOjEzODQzOTEzMjgwNTg1NDgyMjUsInByb3h5IjpudWxsLCJzdWIiOm51bGx9LCJpc3MiOiJSb2Nrb250cm9sLXVuaWZpZWQiLCJleHAiOjE2NDc5MzAyODYsImlhdCI6MTY0NzkyNjY4NiwianRpIjoiMTg2MzYxODE3NDgifQ.Ek5qUfAR83yGoVpEU1NKyx5na9z_UHZKSt8RWzR2yjDShSXDD_qQr9obqk96s28zIScaDIkCO2ZwNFUgeJsRcQ'}
    data = {"eventId": "7bbf6179a10311eca65ffa163e85f750"}
    # data = {"phone": "13113777555", "pwd": "1234567890"}
    # headers = {"Content-Type": "application/x-www-form-urlencoded"}
    result = r.request(url, 'get', param=data, headers=heades)
    print(result)


