import random
import datetime
from time import sleep
import unittest
import HTMLTestRunner
import time
import os
import sys
import demjson


"""随机数"""
def suiji(num):
    """生成num个随机数功能函数"""
    result =[]
    total = 1
    while total <= num:
        temp = random.randint(0, 9)
        if temp not in result:
            result.append(temp)
            total = total + 1
    print(result)
    return result
for i in suiji(5):
    print(i)

"""组合数"""
def zuhe(m,n):
    c = 1
    b = 1
    d = 1
    num2 = 1
    num1 = 1
    num3 = 1
    while c <= m:
        if c <= m:
            num1 = num1 * c
            c = c +1
    while b <= n:
        if b <= n:
            num2 = num2 * b
            b = b + 1
    while d <= m-n:
        if d <= m-n:
            num3 = num3 * d
            d = d + 1
    print(num1,num2,num3)
    num = int(num1 /(num2*num3))
    print(num)
    return num
zuhe(3,2)

"""破译输入数字"""
m = [1,2,3,4,5,6,7,8,9,0]
c = 2
n = []
print(len(n))
a = random.randint(0,9999)
starttime = datetime.datetime.now()
while c > 1:
    num = len(m)-1
    b = random.randint(0,num)
    c = random.randint(0,num)
    d = random.randint(0,num)
    h = random.randint(0,num)
    e = int("%s"%m[b]+"%s"%m[c]+"%s"%m[d]+"%s"%m[h])
    print(e)
    print(len(n))
    if e not in n:
        n.append(e)
        print(n)
        if a == e:
            c = 0
            print(c)
        else:
            c = 3
            print(c)
    else:
        c = 3
        print(c)
        print(n)
endtime = datetime.datetime.now()
print("程序开始时间：", starttime)
print("程序开始时间：", endtime)
print(a)
"""非法字符串json格式化"""
json = '{"result":{"baseId":"","baseState":"","baseCode":"","baseInfo":"","baseMessage":"","baseTime":"","baseSign":"","uid":"67efbdba-8250-5f47-e053-c804650a450c","mobile":"18551698733","mark":"m","yhlx":null,"tk":"15288e4b-5827-4c03-8b7a-b7fa9b019de0","walletId":"67efc172-0866-5f56-e053-c804650aff6d","sjlx":"1"},"state":"0","message":null}'

m = demjson.decode(json)
print(m)