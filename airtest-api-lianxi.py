# -*- encoding=utf8 -*-
__author__ = "Admin"

from airtest.core.api import *
import os

def bug_assert(picture,note,failNote):
    try:
        assert_exists(picture,'测试' + note)
        return True
    except AssertionError:
        snapshot(filename=bug_dir(failNote + '.jpg'))
        print(failNote)
        return False           
def bug_assert_not(picture,note,failNote):    
    try:
        assert_not_exists(picture,'测试' + note)
        return True
    except AssertionError:
        snapshot(filename=bug_dir(failNote + '.jpg'))
        print(failNote)
        return False
def coordinate(l):
    #获取手机尺寸
#     size = os.popen('adb shell wm size').read().split()[2].split('x')
#     phone_width = int(size[1])
#     phone_height = int(size[0])
    #现在连接的手机
    phone_width = 1900
    phone_height = 1050
    # 默认手机尺寸
    default_width = 1900
    default_height = 1050
    if phone_width < default_width:
        a = default_width - phone_width
        a /= default_width
        l[0] = l[0] - round(l[0] * a)
        
    elif phone_width > default_width:
        a = phone_width - default_width        
        a /= default_width        
        l[0] = l[0] + round(l[0] * a)
        
    if phone_height < default_height:
        a = default_height - phone_height
        a /= default_width
        l[1] = l[1] - round(l[1] * a)
        
    elif phone_height > default_height:
        a = phone_height - default_height
        a /= default_width
        l[1] = l[1] + round(l[1] * a)
    return l             
#超时判断
def chaoshi(start_time,timeout=None):
    timeout = timeout or 120
    if (time.time() - start_time) > timeout:
        return False
    else:
        sleep(1)
        return True
#多次划屏
def huaping(num):
    """
    数字1代表向左划屏
    其他代表向右划屏
    """    
    if num == 1:
        for i in range(3):
            swipe([800,500],[1800,500])   #划屏操作
            sleep(1)
    else:
        for i in range(3):
            swipe([1800,500],[800,500])   #划屏操作
            sleep(1)            
#等待判断
def pc_wait(picture,miaoshu,timeout=None):
    start_time = time.time()
    timeout = timeout or 120
    while True:
        if exists(picture):
            assert_exists(picture,miaoshu)
            return True
        else:
            pass
        if (time.time() - start_time) > timeout:
            raise TargetNotFoundError(miaoshu)
            return False
        else:
            time.sleep(0.5)
# 对战类选择倍数
def dianji(picture,timeout=None):  
    start_time = time.time()
    timeout = timeout or 120
    while True:
        if exists(picture):
            touch(picture)
            return True            
        else:
            pass
        if (time.time() - start_time) > timeout:
            raise TargetNotFoundError
            return False
        else:
            time.sleep(1)
# 以出现历史记录弹框做为可以下注的判断          
def tktanchu(picture):  
    start_time = time.time()
    while True:
        if exists(picture):
            sleep(6)
            break
        else:
            if chaoshi(start_time) is False:
                break
def in_youxi(name,picture):  # 进游戏    
    start_time = time.time()
    if name == "qipai":  #选棋牌游戏
        touch(Template(r"tpl1549242702963.png", rgb=True, record_pos=(-0.349, -0.014), resolution=(1920, 1080)))
        sleep(1)
        huaping(1)
        while True:
            if exists(picture):
                touch(picture)
                if exists(Template(r"tpl1550313240943.png", rgb=True, record_pos=(0.002, -0.003), resolution=(1920, 1080))):
                    return False
                                       
                else:
                    return True
                    
            else:
                swipe(coordinate([1800,500]),coordinate([800,500]))   #划屏操作
                sleep(1)
                if chaoshi(start_time) is False:
                    raise TargetNotFoundError('Picture %s not found in screen' % picture)                    
    elif name =="buyu":  #捕鱼游戏
        touch(Template(r"tpl1549246603008.png", rgb=True, record_pos=(-0.348, 0.059), resolution=(1920, 1080)))
        sleep(1)
        huaping(1)
        while True:
            if exists(picture):
                touch(picture)
                if exists(Template(r"tpl1550313240943.png", rgb=True, record_pos=(0.002, -0.003), resolution=(1920, 1080))):
                    return False                   
                else:
                    return True                    
            else:
                swipe(coordinate([1800,500]),coordinate([800,500]))   #划屏操作
                sleep(1)
                if chaoshi(start_time) is False:
                    raise TargetNotFoundError('Picture %s not found in screen' % picture)                                 
    elif name == "jieji":  #街机游戏
        touch(Template(r"tpl1549246711958.png", record_pos=(-0.346, 0.128), resolution=(1920, 1080)))
        sleep(1)
        huaping(2)
        while True:
            if exists(picture):
                touch(picture)
                if exists(Template(r"tpl1550313240943.png", rgb=True, record_pos=(0.002, -0.003), resolution=(1920, 1080))):
                    return False                   
                else:
                    return True               
            else:
                swipe(coordinate([1800,500]),coordinate([800,500]))   #划屏操作 
                sleep(1)
                if chaoshi(start_time) is False:
                    raise TargetNotFoundError('Picture %s not found in screen' % picture)
                    return False                    
    else:
        touch(Template(r"tpl1549246798995.png", rgb=True, record_pos=(-0.346, -0.087), resolution=(1920, 1080)))
        sleep(1)
        huaping(1)
        while True:
            if exists(picture):
                touch(picture)
                if exists(Template(r"tpl1550313240943.png", rgb=True, record_pos=(0.002, -0.003), resolution=(1920, 1080))):
                    return False
                else:
                    return True                    
            else:                
                swipe([1800,500],[800,500])   #划屏操作
                sleep(1)
                if chaoshi(start_time) is False:
                    raise TargetNotFoundError('Picture %s not found in screen' % picture)
                    return False                
#输出设备uuid
def shebei():
    shebei = os.popen('adb devices').readlines()
    devlist = []  
    for i in range(len(shebei)):
        if shebei[i].find('\tdevice') != -1:
            temp = shebei[i].split('\t')
            devlist.append(temp[0])
    return devlist
#更新
def hotgeng(name=None,picture=None):
    if name =="qipai" :
        touch(Template(r"tpl1550630954097.png", record_pos=(-0.348, -0.024), resolution=(1920, 1080)))
        sleep(1)
        for i in range(15):
            if exists(Template(r"tpl1550630978781.png", rgb=True, record_pos=(-0.094, -0.092), resolution=(1920, 1080))):
                touch(Template(r"tpl1550630978781.png", rgb=True, record_pos=(-0.094, -0.092), resolution=(1920, 1080)))
            else:
                
                swipe([1800,500],[800,500])   #划屏操作
    elif name =="buyu":
        touch(Template(r"tpl1550631033213.png", record_pos=(-0.348, 0.054), resolution=(1920, 1080)))
        sleep(1)
        for i in range(5):
            if exists(Template(r"tpl1550630978781.png", rgb=True, record_pos=(-0.094, -0.092), resolution=(1920, 1080))):
                touch(Template(r"tpl1550630978781.png", rgb=True, record_pos=(-0.094, -0.092), resolution=(1920, 1080)))
            else:
                
                swipe([1800,500],[800,500])   #划屏操作
    else:
        touch(Template(r"tpl1550631047595.png", record_pos=(-0.347, 0.131), resolution=(1920, 1080)))
        sleep(1)
        for i in range(5):
            if exists(Template(r"tpl1550630978781.png", rgb=True, record_pos=(-0.094, -0.092), resolution=(1920, 1080))):
                touch(Template(r"tpl1550630978781.png", rgb=True, record_pos=(-0.094, -0.092), resolution=(1920, 1080)))
            else:
                
                swipe([1800,500],[800,500])   #划屏操作


                
"""获取当前打开app包名"""
app = os.popen('adb shell dumpsys window | findstr mCurrentFocus')

"""获取当前连接设备"""
shebei = os.popen('adb devices').readlines()
for i in range(len(shebei)):
        if shebei[i].find('\tdevice') != -1:
            temp = shebei[i].split('\t')
            DEV = temp[0]
"""连接设备"""
connect_device("Android://127.0.0.1:5037/%s"%shebei()[0])  

"""获取当前设备上所有app包名"""
print()

"""卸载app"""            
uninstall('org.cocos2d.test102_test')

"""安装app"""
install('D:\\app\\ceshi\\test102_test-release-signed3.apk')
"""
如果存在app，报AdbError错误
"""
try:
    install('D:\\app\\ceshi\\test102_test-release-signed2.apk')
except Exception:
    uninstall('D:\\app\\ceshi\\test102_test-release-signed2.apk')
    install('D:\\app\\ceshi\\test102_test-release-signed2.apk')

"""设备上app"""
list = device().list_app(third_only=True)
result = []
for i in list:
    if i.startswith("org.cocos2d"):
        result.append(i)
print(result)

"""启动和关闭app"""
start_app('org.cocos2d.test102_test')   #启动
stop_app('org.cocos2d.test102_test')   #关闭

"""获得手机里面某个apk的应用信息、版本信息"""
os.popen('adb shell dumpsys package app')  #app是包名
os.popen('adb shell dumpsys')  #是列出手机上所以包名


"""adb启动apk"""
os.popen('adb shell am start -n breakan.test/breakan.test.TestActivity')

"""adb启动和关闭设备"""
os.popen('adb reboot')  #重启
os.popen('adb shell reboot -p')  #关闭
os.popen('adb shutdown')  #关闭




