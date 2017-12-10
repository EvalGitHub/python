#coding:utf-8


import random #生产随机数

from PIL import Image ,ImageDraw,ImageFont,ImageFilter

#image:负责处理图片
#image:处理画笔
#imageFont :负责处理文字字体
#imageFilter :负责处理率滤镜


# 项目步骤
#1.定义图片
img=Image.new("RGB",(150,50),(255,255,255))
'''
采用rgb模式
图片大小
拓片颜色
'''

#2.创建画笔
draw=ImageDraw.Draw(img)

#3.绘制线条和点
for i in range(random.randint(1,10)):
    draw.line(
        [
            (random.randint(1,150)),(random.randint(1,150)),
            (random.randint(1,150)),(random.randint(1,150)),
        ],
        fill=(10,10,10)

    )
    #绘制点
for i in range(1000):
    draw.point(
        [
            random.randint(1,150),
            random.randint(1,150),
        ],
        fill=(0, 0, 0)
    )

#4.绘制文字
    #随你产生文字（个数一定）
font_list =list("abcdefghijklmnopqrstuvwsyzABCDEFGHIJKLMNOPQRSTUVWSYZ0123456789")

c_chars="".join(random.sample(font_list,5))#random.sample:在制定的列表中随机去出指定的字符个数
    #绘制字体
font= ImageFont.truetype("simsun.ttc",26)
    #字体，font-size
draw.text((5,5),c_chars,font=font,fill="green")
'''
文字的位置：距离上和左的位置
文字内容
代表的字体
字体颜色
'''

#5.定义扭曲的参数
params=[
    1-float(random.randint(1,2))/100,
    0,0,0,
    1-float(random.randint(1,2))/100,
    float(random.randint(1,2))/500,
    0.001,
    float(random.randint(1, 1)) / 500,
    ]

#6.使用滤镜
img = img.transform((150,50),Image.PERSPECTIVE,params)
'''
    扭曲的范围
    扭曲的样式
    扭曲的参数
'''
    #进行扭曲
img= img.filter(ImageFilter.EDGE_ENHANCE_MORE)


img.show()
