import os,sys
import unittest
# print(sys.path)
import time
import HTMLTestRunner
# def test():
#     suite = unittest.TestSuite()
#     # test_path = os.path.dirname(__file__)  #获取脚本执行路径
#     list = ['zhajinhua','feiqinzoushou']
#     for i in list:
#         test_path = "E:\\python-jiaoben\\test\\airtest-test\\%s\\" %i # \\airtest-test
#         test_dir = unittest.defaultTestLoader.discover(test_path, pattern='test_*.py', top_level_dir=None)
#         print(test_dir)
#         suite.addTests(test_dir)
#     return suite
# # suite = unittest.TestSuite()
# now = time.strftime("%Y-%m-%d %H-%M-%S")
# filename = "E:\\python-jiaoben\\test\\baogao\\" + now + ".html"
# fp = open(filename, "wb+")
# runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="用例集合", description="用例执行情况:")
# runner.run(test())
# fp.close()
#     for testsuite in testdir:
#         for testcase in testsuite:
#             suite.addTests(testcase)
#     return suite
# if __name__ == "__main__":
#     runner = unittest.TextTestRunner()
#     runner.run(test())

#
# class RunTools:
#     def chooseAllCases(self, pattern):
#         '''
#         获取TestCases下所有的测试用例
#         :param pattern: 匹配模式
#         :return: 测试用例集
#         '''
#         discover_all_cases = unittest.defaultTestLoader.discover("E:\\python-jiaoben\\airtest-test\\", pattern=pattern,
#                                                                  top_level_dir=None)  # testcase_path是测试用例的根目录
#         return discover_all_cases
#
#
#
# runtools = RunTools()
# b = runtools.chooseAllCases('*.py')
# print(b)
#
# dir = os.path.realpath(__file__)
# print(dir)
# print(dir)
#
#
# dir ='E:\\python-jiaoben\\test\\airtest-test\\'
# li = []
# pys =[]
# for f in os.listdir(dir):
#         if f.endswith(".air"):
#             f = os.path.join(dir, f)
#             # print(f)
#             if os.path.isdir(f):
#                 li.append(f)
# # print(li)
# for s in li:
#     for f in os.listdir(s):
#         if f.endswith(".py") and not f.startswith("__"):
#                 pys.append(os.path.join(s, f))
# print(pys)
# suite = unittest.TestSuite()
#
# # 添加脚本
# for py in pys:
#     suite.addTest(py)


# li=[]
# def getfilename(path):
#     """获取所有用例名称"""
#     pys = []
#     py = []
#     file = os.listdir(path)
#     # print(file)
#     # print(file)
#     for i in file:
#         # print(os.path.splitext(i))
#         if os.path.splitext(i)[1] == ".air":
#             # print(i.replace('.air', ''))
#             li.append(i.replace('.air', ''))
#     for f in os.listdir(path):
#         if f.endswith(".air"):
#             f = os.path.join(path, f)
#             if os.path.isdir(f):
#                 py.append(f)
#     print(py)
#     for s in path:
#         for f in os.listdir(path):
#             if f.endswith(".py") and not f.startswith("__"):
#                 pys.append(os.path.join(s, f))
#     print(pys)
#     return pys
# getfilename('E:\\python-jiaoben\\test\\airtest-test\\')
# path ='E:\\python-jiaoben\\test\\airtest-test\\'
# for root , dirs,files in os.walk(path):
#     for f in files:
#         if os.path.splitext(f)[1] == '.py':
#             os.chdir(root)





import unittest

class TEST():

    def setUp(self):
        print("\n")
        print("test_case_start")

    def test_1_step(self):
        print("test_1_step_start")

    def test_2_step(self):
        print("test_2_step_start")
TEST().test_1_step()
TEST().test_2_step()
#
# if __name__ == '__main__':
#     unittest.main()
# suite = unittest.TestSuite()
# list = youxi().methods()
# num = []
# for j in list:
#     if j.startswith("test_"):
#         num.append(j)
# print(num)
# for i in num:
#         suite.addTest(youxi(i))
# unittest.TextTestRunner().run(suite)


from locust import HttpLocust, TaskSet

def login(l):
    l.client.post("/login", {"username":"ellen_key", "password":"education"})

def logout(l):
    l.client.post("/logout", {"username":"ellen_key", "password":"education"})

def index(l):
    l.client.get("/")

def profile(l):
    l.client.get("/profile")

class UserBehavior(TaskSet):
    tasks = {index: 2, profile: 1}

    def on_start(self):
        login(self)

    def on_stop(self):
        logout(self)

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000


from locust import HttpLocust, TaskSet, task
from random import randint

# Web性能测试
class UserBehavior(TaskSet):

    def on_start(self):
        self.login()

    # 随机返回登录用户
    def login_user(self):
        users = {"user1":123456,"user2":123123,"user3":111222}
        data = randint(1, 3)
        username = "user"+str(data)
        password = users[username]
        return username, password

    @task
    def login(self):
        username, password = self.login_user()
        self.client.post("/login_action", {"username":username, "password":password})


class User(HttpLocust):
    task_set = UserBehavior
    min_wait = 1000
    max_wait = 3000
    host = "http://www.xxx.com"

import sys
import timeit


# 使用insert创建1~1000的数组

# def insert_num():
#     thousand_list1 = list()
#     for i in range(1, 1001):
#         thousand_list1.insert(len(thousand_list1), i)
#     #print (thousand_list1)
#
# # 使用append创建1~1000的数组
# def append_num():
#     thousand_list2 = list()
#     for i in range(1, 1001):
#         thousand_list2.append(i)
#     #print("append_num",thousand_list2)
#
# #使用列表生成式生成
#
# def main():
#     num = 10000000
#     in_obj = timeit.Timer("insert_num()","from __main__ import insert_num")
#     print("使用insert方法往列表插入1至1000, 方法反复执行%d次共耗时:"%num,in_obj.timeit(number=num),"秒")
#
#     in_obj = timeit.Timer("append_num()","from __main__ import append_num")
#     print("使用append方法依次往列表插入1至1000,方法反复执行 %d次共耗时:"%num,in_obj.timeit(number=num),"秒")
# if __name__ == "__main__":
#     main()
print(time.strftime("%Y-%m-%d %H-%M-%S"))

print(1/7)


import datetime
starttime=datetime.datetime.now()
print("程序开始时间：",starttime)
endtime=datetime.datetime.now()
print("程序结束时间：",starttime)
second=(endtime-starttime).seconds
print("执行完程序用时",second,"s")


"""统计app打开正常次数"""
from airtest.core.api import *
import datetime
import xlwt
import xlrd
shebei ={}
shebei[50] = "d261e577"
def ceshi():   #坐标登录
        connect_device("Android://127.0.0.1:5037/1f2a977c0704")   #连接手机
        wake() #唤醒屏幕
        starttime=datetime.datetime.now()
        hao = 0
        huai = 0
        stop_app('org.cocos2d.huihuang_online')
        start_app('org.cocos2d.huihuang_online')
        for i in range(1):
            sleep(30)
            try:
                assert_exists(Template(r"tpl1548726662856.png", record_pos=(-0.109, 0.172), resolution=(1920, 1080)),"成功打开app且展示正常")
                hao = hao + 1
            except AssertionError:
                huai = huai + 1
            stop_app('org.cocos2d.huihuang_online')
            start_app('org.cocos2d.huihuang_online')
        endtime=datetime.datetime.now()
        second=(endtime-starttime).seconds
        print("程序开始时间：",starttime)
        print("程序结束时间：",endtime)
        print("程序运行时间：",endtime)
        a = hao/100
        b = huai/100
        print("打开APP成功概率：{},打开APP失败概率：{}".format(a, b))
# ceshi()

from xlutils.copy import copy
# data = xlrd.open_workbook(u'登录统计.xls')
# table = data.sheets()[0]
# nrows = table.nrows
# ncols = table.ncols
# print(nrows,ncols)
# print(table.cell(1,0).value)

data = xlrd.open_workbook(u'登录统计.xls',formatting_info=True)
new_data = copy(data)
table = new_data.get_sheet(0)
table.write(1,1,30)
new_data.save(u'登录统计.xls')



# table.put_cell(1,1,1,20,0)
# print(table.cell(1,1).value)

import os,time
# def chaoshi(start_time,):
#     while True:
#         c = input("请输入一个数字：")
#         print(type(c))
#         if c == '12':
#             continue
#         if c >= '10':
#             return False
# chaoshi()

#             pc_wait(Template(r"tpl1549105183090.png", rgb=True, record_pos=(-0.078, 0.232), resolution=(1920, 1080)),"进入体验房默认金额为1百万")

# a ="test_aaaa"
# print(a[5:])
# def chaoshi(start_time,timeout=None):
#     timeout = timeout or 120
#     if (time.time() - start_time) > timeout:
#         return False
#     else:
#         return True
#
# start_time = time.time()
# n = 0
# while True:
#     if 1 > 3:
#         break
#     else:
#         print(n+1)
#         print(time.time())
#         if chaoshi(start_time,16) is False:
#             break

li = []
pys = []
def getfilename(path):
    """获取所有用例名称"""
    """
    os.listdir(dirname)：列出dirname下的目录和文件 
    os.getcwd():获得当前工作目录 
    os.curdir('.'):返回当前目录
    os.chdir(dirname):改变工作目录到dirname 
    os.path.isdir(name):判断name是不是一个目录，name不是目录就返回false
    os.path.isfile(name):判断name是不是一个文件，不存在name也返回false
    os.path.exists(name):判断是否存在文件或目录name 
    os.path.getsize(name):获得文件大小，如果name是目录返回0L
    os.path.abspath(name):获得绝对路径 
    os.path.normpath(path):规范path字符串形式 
    os.path.split(name):分割文件名与目录（事实上，如果你完全使用目录，它也会将最后一个目录作为文件名而分离，同时它不会判断文件或目录是否存在） 
    os.path.splitext():分离文件名与扩展名 
    os.path.join(path,name):连接目录与文件名或目录 
    os.path.basename(path):返回文件名 
    os.path.dirname(path):返回文件路径 
    os.remove()函数用来删除一个文件
    """
    suites = []
    file = os.listdir(path)
    print(file)
    for f in file:
        if f.endswith(".air") and not f.startswith("key"):
            li.append(f.replace('.air', ' '))
            if os.path.isdir(f):
                suites.append(f)
    print(suites)
    for i in file:
        if os.path.splitext(i)[1] == " ":
            pys.append(i.replace('.air', ' '))
    # for f in os.listdir(path):
    #     if f.endswith(".air"):
    #         f = os.path.join(path, f)
    #         if os.path.isdir(f):
    #             py.append(f)
    # print(py)
    # for s in py:
    #     for f in os.listdir(s):
    #         if f.endswith(".air") and not f.startswith("a"):
    #             pys.append(os.path.join(s, f))


getfilename('E:\\python-jiaoben\\test\\airtest-test\\')
dir = os.path.dirname(os.path.realpath(__file__))
print(dir)


# import unittest
# memblist = ['FunctionTestCase', 'TestCase', 'TestLoader', 'TestProgram', 'TestResult',
#  'TestSuite','TextTestRunner', 'defaultTestLoader','findTestCases', 'getTestCaseNames',
#  'main', 'makeSuite']
# for memb in memblist:
#     cur = getattr(unittest, memb)
#     # print(help(cur))
#
#
# def main():
#     for i in range(5):
#         if i == 6:
#            print(1111)
#            return True
#     return False
# if main():
#     print(222222)
# else:
#     print(333333)
import os
path = os.path.abspath('')

print(type(User))

def ceshi(num):
    for i in range(num):
        print(i)
        if i > 5:
            return 1
        else:
            pass

print(type(ceshi(10)))

import math
#闲家携带金额
num = {"1":30,"2":30,"3":10000}
#闲家最大输钱倍数
result = {}
#闲家下注的最大倍数
zhuMa = {}
#庄家抢庄倍数
beiShu = 200
#房间底注
diZhu = 10
#
#第一种算法
#
for i in num:
    if num[i]/diZhu >beiShu:
        result[i] = beiShu
    else:
        result[i] = math.floor(num[i]/diZhu)  #向下取整
sum = 0
for j in result:
    sum = sum + result[j]
print(sum)
#计算玩家最大下注倍数
if math.floor(result["1"]*beiShu/sum) >=result["1"]:
    zhuMa["1"] = result["1"]
else:
    zhuMa["1"] = int(math.floor(result["1"]*beiShu/sum))
if math.floor(result["2"]*beiShu/sum) >=result["2"]:
    zhuMa["2"] = result["2"]
else:
    zhuMa["2"] = int(math.floor(result["2"]*beiShu/sum))
if math.floor(result["3"]*beiShu/sum) >=result["3"]:
    zhuMa["3"] = result["3"]
else:
    zhuMa["3"] = int(math.floor(result["3"]*beiShu/sum))

print(zhuMa)

#
#第二种算法
#
#闲家最大输钱倍数
result_1 = {}
#闲家下注的最大倍数
zhuMa_1 = {}
for i in num:
    result_1[i] = math.floor(num[i]/diZhu)  #向下取整
sum_1 = 0
for j in result_1:
    sum_1 = sum_1 + result_1[j]
print(sum_1)
#计算玩家最大下注倍数
zhuMa_1["1"] = int(math.floor(result_1["1"]/sum_1*beiShu))
zhuMa_1["2"] = int(math.floor(result_1["2"]*beiShu/sum_1))
zhuMa_1["3"] = int(math.floor(result_1["3"]*beiShu/sum_1))
print(zhuMa_1)


#向上取整
print("2.3向上取整:",math.ceil(2.3))
print("2.6向上取整:",math.ceil(2.6))

#向下取整
print("2.3向下取整:",math.floor(2.3))
print("2.6向下取整:",math.floor(2.6))

#四舍五入
print("2.3四舍五入:",round(2.3))
print("2.6四舍五入:",round(2.6))

#这三个的返回结果
print(type(math.ceil(2.3)))
print(type(math.floor(2.6)))
print(type(round(2,2)))
print(round(2,2))

#保留2位小数
a = 13.9499999
print("%.3f"%a)
print(type("%.3f"%a))


for i in range(10):
    print("move%s"%i)