#coding:utf-8

#1.python 文件
    #1.创建文件对象
    #2.对文件对象进行操作
    #3.关闭文件


 #创建文件对象
    #open
        #path 文件的路径
        #method 文件的权限
            #r 读
            #w 写
            #a 追加写
            #rb 二进制读
            #rw 二进制写
        #buffering 是否缓存
#f=open("1.txt","r")
#f.read()读取全文
#f.readline()读取一行
# f.readlines以行为单位读取全文
#f.close()



#2，difflib
    #differ
    # HtmlDiff  形成比对html

   #指定比对内容
    #compare 输出比对结果
    #make_file 将比对结果形成文件

#3.sys
    #sys.argv 用来接收外部运行脚本传递的参数



#4.if__name__ =="__main__"
    #如果文件自己执行

    #如果文件自己执行__name__的值为__main__
    #如果文件被当作脚本执行 __name__的值为文件名

import sys
import difflib

#接受命令行传递的两个文件路径
first_path = sys.argv[0]
next_path = sys.argv[1]

with open(first_path,"r",errors="ignore") as f:
    first_path = f.readlines()

with open(next_path,"r",errors="ignore") as f:
    next_path = f.readlines()


#创建比对对象
diff =difflib.HtmlDiff()
html =diff.make_file(first_path,next_path)
#print(html)
#将比对结果输出一个文见
with open("dif.html",'w') as f:
    f.write(html)


"""

diff =difflib.Differ()
content = diff.compare(first_path,next_path)
for i in content:
    print(i)
"""