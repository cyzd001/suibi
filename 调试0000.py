import cx_Oracle as oracle

"""商家类型为1,2（商家和摊位）"""
db = oracle.connect('pj_core', 'pj_core', '192.168.55.5:1521/ljcprd')
cur = db.cursor()
cur.execute("select a.SQDLZH,b.SYR_SJRWJBXX_ID,b.SYR_SYZTJC_ID from SYR_SQGX a,SYR_SJYGJBXX b, SYR_SJRWJBXX c where b.SYR_SJRWJBXX_ID(+) = c.ID and c.sjlx = 1 and b.SYR_SQGX_ID=a.ID ")
row = cur.fetchone()
# print(row[0])
print(row)
db.close()
db = oracle.connect('pj_extbank', 'pj_extbank', '192.168.55.5:1521/ljcprd')
cur = db.cursor()
cur.execute("select a.FRZJH,a.FRXM,d.ZHH from EXT_SJRWJBXX a,EXT_SYZTJC b,EXT_SJGLZHGX c,EXT_SJSKZHJCXX d where a.id=b.EXT_SJRWJBXX_ID and b.ID=c.EXT_ZT_SJ_ID and c.EXT_SJSKZHJCXX_ID=d.ID and a.id='74570757-5651-4f37-a62c-7628d24a3fd0'")
row1 = cur.fetchone()
# print(row[0])
print(row1)
db.close()
db = oracle.connect('pj_core', 'pj_core', '192.168.55.5:1521/ljcprd')
cur = db.cursor()
cur.execute("select a.SQDLZH,b.SYR_SJRWJBXX_ID,b.SYR_SYZTJC_ID from SYR_SQGX a,SYR_SJYGJBXX b, SYR_SJRWJBXX c where b.SYR_SJRWJBXX_ID(+) = c.ID and c.sjlx = 2 and b.SYR_SQGX_ID=a.ID")
row = cur.fetchone()
# print(row[0])
print(row)
db.close()
db = oracle.connect('pj_extbank', 'pj_extbank', '192.168.55.5:1521/ljcprd')
cur = db.cursor()
cur.execute("select a.FRZJH,a.FRXM,d.ZHH from EXT_SJRWJBXX a,"
            "EXT_SYZTJC b,EXT_SJGLZHGX c,EXT_SJSKZHJCXX d where a.id=b.EXT_SJRWJBXX_ID and b.ID=c.EXT_ZT_SJ_ID and c.EXT_SJSKZHJCXX_ID=d.ID and a.id='4638ab4d-7872-4a3b-9096-0e923d487174'")
row2 = cur.fetchone()
# print(row[0])
print(row2)
db.close()
"""商家类型为3（团体总店）"""
db = oracle.connect('pj_core', 'pj_core', '192.168.55.5:1521/ljcprd')
cur = db.cursor()
cur.execute("select a.SQDLZH,b.SYR_SJRWJBXX_ID,b.SYR_SYZTJC_ID from SYR_SQGX a,SYR_SJYGJBXX b, SYR_SJRWJBXX c where b.SYR_SJRWJBXX_ID(+) = c.ID and c.sjlx = 3 and b.SYR_SQGX_ID=a.ID and b.SYR_SYZTJC_ID is null")
row = cur.fetchall()
print(row)
db.close()
db = oracle.connect('pj_extbank', 'pj_extbank', '192.168.55.5:1521/ljcprd')
cur = db.cursor()
cur.execute("select frxm,frzjh,yyzzmc from  EXT_SJRWJBXX  where ID=%r"%row[0][1])
row3 = cur.fetchone()
print("商家类型为3（团体总店）:",row3)

"""商家类型为3（团体网店）"""
# db = oracle.connect('pj_core', 'pj_core', '192.168.55.5:1521/ljcprd')
# cur = db.cursor()
# cur.execute("select a.SQDLZH,b.SYR_SJRWJBXX_ID,b.SYR_SYZTJC_ID from SYR_SQGX a,SYR_SJYGJBXX b, SYR_SJRWJBXX c where b.SYR_SJRWJBXX_ID(+) = c.ID and c.sjlx = 3 and b.SYR_SQGX_ID=a.ID and b.SYR_SYZTJC_ID is not null")
# row = cur.fetchone()
# print(row)
# db.close()
db = oracle.connect('pj_extbank', 'pj_extbank', '192.168.55.5:1521/ljcprd')
cur = db.cursor()
cur.execute("select d.ZHKHM,d.KHZJH,d.zhh from EXT_SJGLZHGX c,EXT_SJSKZHJCXX d where  c.EXT_SJSKZHJCXX_ID=d.ID and c.EXT_ZT_SJ_ID='bf0c4dd0-e1d0-4d5e-a680-c57382259b71'")
row4 = cur.fetchone()
print("商家类型为3（团体网店）:",row4[0],row4[1],row4[2])
"""商家类型为4（连锁总店）"""
db = oracle.connect('pj_core', 'pj_core', '192.168.55.5:1521/ljcprd')
cur = db.cursor()
cur.execute("select a.SQDLZH,b.SYR_SJRWJBXX_ID,b.SYR_SYZTJC_ID from SYR_SQGX a,SYR_SJYGJBXX b, SYR_SJRWJBXX c where b.SYR_SJRWJBXX_ID(+) = c.ID and c.sjlx = 4 and b.SYR_SQGX_ID=a.ID and b.SYR_SYZTJC_ID is  null")
j = cur.fetchall()
print(j)
db.close()
db = oracle.connect('pj_extbank', 'pj_extbank', '192.168.55.5:1521/ljcprd')
cur = db.cursor()
cur.execute("select a.FRZJH,d.ZHKHM,d.ZHH from EXT_SJRWJBXX a,EXT_SJGLZHGX c,EXT_SJSKZHJCXX d where a.id=c.EXT_ZT_SJ_ID and c.EXT_SJSKZHJCXX_ID=d.ID and a.ID='6612d948-bf61-4a9b-b5aa-3570479634cb'")
row5=cur.fetchone()
print("商家类型为4（连锁总店):",row5[0],row5[1],row5[2])
db.close()

"""商家类型为4（连锁分店）"""
db = oracle.connect('pj_core', 'pj_core', '192.168.55.5:1521/ljcprd')
cur = db.cursor()
cur.execute("select a.SQDLZH,b.SYR_SJRWJBXX_ID,b.SYR_SYZTJC_ID from SYR_SQGX a,SYR_SJYGJBXX b, SYR_SJRWJBXX c where b.SYR_SJRWJBXX_ID(+) = c.ID and c.sjlx = 4 and b.SYR_SQGX_ID=a.ID and b.SYR_SYZTJC_ID is NOT  null")
row = cur.fetchall()
print(row[20])
db.close()
db = oracle.connect('pj_core', 'pj_core', '192.168.55.5:1521/ljcprd')
cur = db.cursor()
cur.execute("select a.SQDLZH,b.SYR_SJRWJBXX_ID,b.SYR_SYZTJC_ID from SYR_SQGX a,SYR_SJYGJBXX b, SYR_SJRWJBXX c where b.SYR_SJRWJBXX_ID(+) = c.ID and c.sjlx = 4 and b.SYR_SQGX_ID=a.ID and b.SYR_SJRWJBXX_ID=%r"%row[20][1])
row6= cur.fetchone()
print("连锁分店对应总店信息:",row6[0],row6[1],row6[2])
db.close()
db = oracle.connect('pj_extbank', 'pj_extbank', '192.168.55.5:1521/ljcprd')
cur = db.cursor()
cur.execute("select a.FRZJH,d.ZHKHM,d.ZHH from EXT_SJRWJBXX a,EXT_SJGLZHGX c,EXT_SJSKZHJCXX d where a.id=c.EXT_ZT_SJ_ID and c.EXT_SJSKZHJCXX_ID=d.ID and a.ID=%r"%row6[1])
row7=cur.fetchone()
print("连锁分店对应总店信息:",row7[0],row7[1],row7[2])
db.close()
db = oracle.connect('pj_rep', 'pj_rep', '192.168.55.5:1521/ljcprd')
cur = db.cursor()
cur.execute("select * from (select * from BUS_JGTZYHZ  where TZS !=0 or RWS !=0 or BHS !=0 or JHS !=0 order by TJYF desc) where SYR_TZJGCS_ID='0000013443'")
row8=cur.fetchone()
print(row8)
db.close()
#
# import random
# a = []
# b = []
# a.append(b)
# b.append(b)
# print (a)
# print (b)
# a=[1,3,5,6,7]                # 将序列a中的元素顺序打乱
# random.shuffle(a)
# print(a)



# '15383810004', '8d54dc3a-f8c4-489d-8e3f-24bc70c31e46'
# db = oracle.connect('pj_extbank', 'pj_extbank', '192.168.55.5:1521/ljcprd')
# cur = db.cursor()
# cur.execute("select ,a.FRXM,d.ZHH from EXT_SJRWJBXX a,"
#             "EXT_SYZTJC b,EXT_SJGLZHGX c,EXT_SJSKZHJCXX d where a.id=b.EXT_SJRWJBXX_ID and b.ID=c.EXT_ZT_SJ_ID and c.EXT_SJSKZHJCXX_ID=d.ID and sjh=%s"%num2)
# row = cur.fetchall()
# # print(row[0])
# for i in row:
#     print(i[0],i[1],i[2])




# from tkinter import *
#
# top=Tk()
# top.wm_title("菜单")
# top.geometry("400x300+300+100")
#
# # 创建一个菜单项，类似于导航栏
# menubar=Menu(top)
#
# # 创建菜单项
# fmenu1=Menu(top)
# for item in ['新建','打开','保存','另存为']:
#     # 如果该菜单时顶层菜单的一个菜单项，则它添加的是下拉菜单的菜单项。
#     fmenu1.add_command(label=item)
#
# fmenu2=Menu(top)
# for item in ['复制','粘贴','剪切']:
#     fmenu2.add_command(label=item)
#
# fmenu3=Menu(top)
# for item in ['默认视图','新式视图']:
#     fmenu3.add_command(label=item)
#
# fmenu4=Menu(top)
# for item in ["版权信息","其他说明"]:
#     fmenu4.add_command(label=item)
#
# # add_cascade 的一个很重要的属性就是 menu 属性，它指明了要把那个菜单级联到该菜单项上，
# # 当然，还必不可少的就是 label 属性，用于指定该菜单项的名称
# menubar.add_cascade(label="文件",menu=fmenu1)
# menubar.add_cascade(label="编辑",menu=fmenu2)
# menubar.add_cascade(label="视图",menu=fmenu3)
# menubar.add_cascade(label="关于",menu=fmenu4)
#
# # 最后可以用窗口的 menu 属性指定我们使用哪一个作为它的顶层菜单
# top['menu']=menubar
# top.mainloop()

import tkinter as tk
from tkinter import Menu    # 导入菜单类


# win = tk.Tk()
# win.title("Python GUI")    # 添加标题
#
#
# def _quit():
#     """结束主事件循环"""
#     win.quit()      # 关闭窗口
#     win.destroy()   # 将所有的窗口小部件进行销毁，应该有内存回收的意思
#     exit()
#
# # 创建菜单栏功能
# menuBar = Menu(win)
# win.config(menu=menuBar)
#
#
# # 创建一个名为File的菜单项
# fileMenu = Menu(menuBar, tearoff=0)
# menuBar.add_cascade(label="File", menu=fileMenu)
#
# # 在菜单项File下面添加一个名为New的选项
# fileMenu.add_command(label="New")
#
# # 在两个菜单选项中间添加一条横线
# fileMenu.add_separator()
#
# # 在菜单项下面添加一个名为Exit的选项
# fileMenu.add_command(label="Exit", command=_quit)
#
# # 在菜单栏中创建一个名为Help的菜单项
# helpMenu = Menu(menuBar, tearoff=0)
# menuBar.add_cascade(label="Help", menu=helpMenu)
# # 在菜单栏Help下添加一个名为About的选项
# helpMenu.add_command(label="About")
#
# win.mainloop()      # 进入主事件循环，当调用mainloop()时,窗口才会显示出来
# import plot
# explode = (0.05, 0, 0, 0)
# labels = [u'Canteen', u'Supermarket', u'Dorm', u'Others']
# sizes = [73, 21, 4, 2]
# colors = ['red', 'yellow', 'blue', 'green']
#
# patches, l_text, p_text = plot.pie(sizes, explode=explode, labels=labels, colors=colors,
#                                    labeldistance=1.1, autopct='%2.0f%%', shadow=False,
#                                    startangle=90, pctdistance=0.6)
# for t in l_text:
#     t.set_size = 30
# for t in p_text:
#     t.set_size = 20
# plot.axis('equal')
# plot.legend(loc='upper left', bbox_to_anchor=(-0.1, 1))
# plot.grid()
# plot.show()


# b = [chr(i) for i in range(97,123)]
# result=[]
# for i in range(1,101):
#     for j in b:
#         num= '%s'%i + '%s'%j
#         result.append(num)
# print(result)
# print(len(result))
#
# import operator as op
# if (op.gt("123","100")):
#     print("greater than")
# if(op.lt("100","123")):
#     print("less than")
import random,time
def createPhoneCode(session):
    chars=['0','1','2','3','4','5','6','7','8','9']
    x = random.choice(chars),random.choice(chars),random.choice(chars),random.choice(chars)
    verifyCode = "".join(x)
    session["phoneVerifyCode"] = {"time":int(time.time()), "code":verifyCode}
    return verifyCode
chars=['0','1','2','3','4','5','6','7','8','9']
for i in range(1,10):
    x = random.choice(chars), random.choice(chars), random.choice(chars), random.choice(chars)
    verifyCode = "".join(x)
    print(verifyCode)
