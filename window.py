#pip3 install cs_Freeze

'''
Tk:窗口
Button:按钮
Entry:输入框
Label：
Text:文本域
'''
from tkinter import Tk,Button,Entry,Label,Text,END


#from main import youdaohelp

#创建一个窗口对象


class Application(object):
    def __init__(self):
        self.helper = youdaohelp()
        # 创建一个窗口对象
        self.window = Tk()
        self.window.title(u"知了词典")
        self.window.geometry("280x350+600+250")  # 窗口的宽高，x，y坐标

        # 输入狂
        self.entry = Entry(self.window)
        # pack grid place
        self.entry.place(x=10, y=10, width=200, height=25)

        # 提交按钮
        self.submit_btn = Button(self.window, text=u"查询",command=self.submit)
        self.submit_btn.place(x=220, y=10, width=50, height=25)

        # 翻译结果标题
        self.title_label = Label(self.window, text="翻译结果")
        self.title_label.place(x=10, y=55, height=25)

    

        # 显示翻译结果区域
        self.result_text = Text(self.window, background="#ccc")
        self.result_text.place(x=10, y=75, width=260, height=250)



    def submit(self):
        #1）从输入框获取输入的值
        content = self.entry.get()#获得输入值
        #print(content)

        #2)把这个值传给服务器验证
        res =self.helper.crawl(content)

        #3)把结果放置底部的Text控件中
        #删除之前输入的值(从开始到末尾)
        self.result_text.delete(1.0,END)
        self.result_text.insert(END,res)

    def run(self):
        self.window.mainloop()




import urllib.request

import urllib.parse

import time

import random

import hashlib

import json

#from window import Application


class youdaohelp(object):
    def __init__(self):
        pass

    def crawl(self,content):
        # 获得是秒
        timestamp = int(time.time() * 1000) + random.randint(0, 10)
        # content= input("请输入要翻译的文字：")
        u = "fanyideskweb"
        d = content
        f = str(timestamp)
        c = "rY0D^0'nM0}g5Mm1z%1G4"
        salt = hashlib.md5((u + d + f + c).encode("utf-8")).hexdigest()
        data = {
            "i": content,
            "from": "AUTO",
            "to": "AUTO",
            "smartresult": "dict",
            "client": "fanyideskweb",
            # "salt":"1512810220017",
            "salt": timestamp,
            "sign": salt,
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "action": "FY_BY_CLICKBUTTION",
            "typoResult": "false"
        }
        data = urllib.parse.urlencode(data).encode('utf-8')

        url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&sessionFrom="
        request = urllib.request.Request(url=url, method="POST", data=data)
        response = urllib.request.urlopen(request)
        #print(response.read().decode('utf-8'))

        result_str = response.read().decode('utf-8')
        result_dict = json.loads(result_str)#将字符串转换成一个json 数据

        return result_dict['translateResult'][0][0]['tgt']




if __name__ =="__main__":
     app = Application()
     app.run()