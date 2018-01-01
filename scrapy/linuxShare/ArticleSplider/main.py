#调试

from scrapy.cmdline import  execute
import sys
import os

#os.path.abspath(__filename__).当前文件的路径
#os.path.dirname()当前文件的父级文件路径

#主要目的是动态的配置爬虫文件路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy","crawl","jobbole"])