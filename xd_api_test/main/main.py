# coding = utf-8


from package import HTMLTestRunner_cn
import unittest
# from xd_api_test.case.test_InspectorEvent import *
'''
test
test_Global_Management
'''
#定义要执行的测试用例的路径
test_dir =r'F:\xd_api_test\xd_api_test\case'
#定义要执行的测试用例的路径和名称格式
#test_*.py的意思是，./testcase路径下文件名称格式为test_*.py的文件，*为任意匹配，路径下有多少的test_*.py格式的文件，就依次执行几个
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')
#定义测试报告的名称和存储位置
filename = r'F:\xd_api_test\test_report\loginReport.html'

#开始执行
if __name__ == '__main__':

    #suit=unittest.TestSuite()
   # suit.addTest(Test_01("test_01"))


    #以wb(可写的二进制文件)形式，打开文件，若文件不存在，则先执行创建，再执行打开
    fp = open(filename, 'wb')
    #调用HTMLTestRunner生成报告
    runner = HTMLTestRunner_cn.HTMLTestRunner(
        # 指定测试报告的文件
        stream=fp,
        # 测试报告的标题
        title="动态巡查管控系统",
        # 测试报告的副标题
        description="动态巡查管控系统"
    )
    #执行用例
    runner.run(discover)
    fp.close()

#if __name__ == '__main__':
  #  app = XdclassTestCase()
   # app.runAllCase("小滴课堂")





