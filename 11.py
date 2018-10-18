from tkinter import *
from tkinter import ttk
import tkinter as tk
import json
import requests
from tkinter import messagebox

def jiemian_info():
    ws = jiemian.winfo_screenwidth()
    hs = jiemian.winfo_screenheight()
    x = (ws / 2) - 200
    y = (hs / 2) - 200
    print("%d,%d" % (ws, hs))
    return x, y
jiemian = Tk()
jiemian.title("登录小助手")
a, b = jiemian_info()
jiemian.geometry("300x150+%d+%d" % (a, b))
urll = 'http://192.168.18.38:8073/login'
def button1():
    datain = {'SJH':url.get(),'PWD':pwd.get()}
    num = int(url.get())
    print(type(num))
    print(datain)
    m = requests.get(url=urll,data=datain)
    print(m.text)
    print(type(eval(m.text)))
    msg = eval(m.text)
    if msg['msg_code'] == '200':
        a = messagebox.showinfo('提示', '成功登录')
        print(a)
    elif msg['msg_code'] == '204':
        messagebox.showinfo('提示', '密码和用户名错误')
    # a = messagebox.askokcancel('提示', '真的要退出吗？')     #弹框
    # print(a)
    # if a == True:
    #     jiemian.quit()  # 关闭窗口
    #     jiemian.destroy()  # 将所有的窗口小部件进行销毁，应该有内存回收的意思

    print(m.headers)
    print(m.status_code)
Label(jiemian, text="用户：").place(x=55, y=20)
Label(jiemian, text="账号：").place(x=55, y=60)
'''设置文本框'''
url = Entry(jiemian,font=('微软雅黑',10),width=15)
url.place(x=95, y=20)
var_pwd = StringVar()
pwd = Entry(jiemian, font=('微软雅黑',10),width=15)
pwd.place(x=95, y=60)
'''设置按钮'''
Button(jiemian,text="登录",width=10,command=button1).place(x=105, y=95)

# fra = tk.Frame(jiemian)
# label=Label(fra, text="网站：")
# label.place(x=100, y=20)
# var_usr = StringVar()
# usr = Entry(fra, font=('微软雅黑', 10), width=12)
# usr.place(x=150, y=60)
#
# li = ['aus-bank', 'aus-nk-pjcore', 'aus-unionpay', 'aus-nk-bank', 'aus-merchant', 'aus-hcapp', \
#               'aus-web', 'aus-wechat', 'aus-wechat-mp', 'boc-clear', 'aus-qrcode']
# listb = Listbox(jiemian, selectmode=MULTIPLE)
# listb.place(x=150, y=40, relwidth=0.3, relheight=0.5)
# yscrollbar = tk.Scrollbar(listb, command=listb.yview)
# yscrollbar.pack(side=tk.RIGHT, fill=tk.Y)
# listb.config(yscrollcommand=yscrollbar.set)
# for item in li:
#     listb.insert(0, item)
#
# label.place_forget()
# fra.pack()




# Label(jiemian, text="网站：").place(x=100, y=20)
# Label(jiemian, text="用户：").place(x=100, y=60)
# Label(jiemian, text="密码：").place(x=100, y=100)
# Label(jiemian, text="提示：网站没有账号可以选好网站名点击登录直接打开").place(x=70, y=140)
# '''设置文本框'''
# # var_usr = StringVar()
# usr = Entry(jiemian, font=('微软雅黑', 10), width=12)
# usr.place(x=150, y=60)
# # var_pwd = StringVar()
# pwd = Entry(jiemian, font=('微软雅黑', 10), width=12)
# pwd.place(x=150, y=100)
# """设置请求方式下拉框"""
# numberChosen = ttk.Combobox(jiemian, width=10, font=('微软雅黑', 10))
# numberChosen['values'] = ("皮夹", "来聚财", "生意人", "jenkins", "皮夹-电信", "来聚财-电信", "生意人-电信", "模拟银联支付")  # 设置下拉列表的值
# numberChosen.place(x=150, y=20)  # 设置其在界面中出现的位置  column代表列   row 代表行
# numberChosen.current(0)
jiemian.mainloop()

# def hello():
#     print('hello')
# def about():
#     label = Label(root, text='王小涛_同學\n QQ:*********', fg='red', bg='black')
#     label.pack(expand=YES, fill=BOTH)
# root = Tk()
# menubar = Menu(root)
# filemenu = Menu(menubar, tearoff=0)
# filemenu.add_command(label='打开', command=hello)
# filemenu.add_command(label='保存')
# filemenu.add_separator()
# filemenu.add_command(label='退出', command=root.quit)
# menubar.add_cascade(label='文件', menu=filemenu)
# helpmenu = Menu(menubar, tearoff=0)
# helpmenu.add_command(label='关于作者', command=about)
# menubar.add_cascade(label='关于', menu=helpmenu)
# root.config(menu=menubar)
# root.geometry('200x400')
# root.mainloop()
