#coding:utf-8

import xlsxwriter
#安装
#pip3 install xlswriter
'''
#1.创建一个Excel文件（文件名）
work = xlsxwriter.Workbook('1.xlsx')

#2.创建表格(表名)
worksheet = work.add_worksheet('while')

#3.修改内容的格式
    #表格的格式
worksheet.set_column("A:A",20)
    #内容的格式
bold = work.add_format({"bold":True})


#4.写入内容
worksheet.write("A1","while",bold)

    #写入图片
worksheet.insert_image("A12","1.png")


    #写入函数
worksheet.write("A3",2,bold)
worksheet.write("A4",12,bold)
worksheet.write("A4","=SUM(A3:A4)",bold)

#关闭并保存
work.close()

'''


#练习2添加一大串数据

work = xlsxwriter.Workbook('2.xlsx')
worksheet = work.add_worksheet("while")


chart = work.add_chart({"type":"column"})
    #column 柱状图
    #area 面积图
    #bar 条形图
    #line 折线图
    #radar 雷达图

#添加数据
    #1.声明一个数据容器

title='abcdefghi'
for index,name in enumerate(title):
    point = "A%d"%(index+1)
    worksheet.write(point,name)

data = [1, 2, 3, 4, 44, 55, 66, 456]
for i,j in enumerate(data):
    point ="B%d"%(i+1)
    worksheet.write(point,j)

#为图表添加数据
chart.add_series({
    "categories":"=while!$a$1:$a$9",#类别标签的范围
    "values":"=while!$b$1:$b$9",#图表数据的范围
    "line":{"color":"red","background":"green"}#图标线条的属性

})

#现有数据才能插入
worksheet.insert_chart("A10",chart)

work.close()

