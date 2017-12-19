#运行 scrapy crawl  author -o au.json

import scrapy
import json

class QuotesSpider(scrapy.Spider):
    name ='author'
    start_urls=['http://quotes.toscrape.com/']
    #没有使用scrapy.Request(url,self.parse)，默认自动执行parse回调函数
    def parse(self,response):
        for href in response.css('.author + a::attr(href)'):
            yield response.follow(href,self.parse_author)

        for href in response.css("li.next a::attr(href)"):
            #response.follow 可以直接使用相对路径
            yield response.follow(href,self.parse)
            #response.urljoin可以将相对路径转化为绝对路径
            #yield scrapy.Request(response.urljoin(href))

    def parse_author(self,response):
        def extract_width_css(query):
            return response.css(query).extract_first().strip()


        # scrapy crawl author -o au1.json  （命令行的方式）
        yield{
            'name':extract_width_css("h3.author-title::text"),
            'birthdate':extract_width_css(".author-born-date::text"),
           # 'bio':extract_width_css('.author-description::text')
        }
    
        #写入文件json.dumps 对象变字符串（程序直接运行的方式）
        with open("b.json","a") as w:
            w.write(json.dumps({
                'name':extract_width_css("h3.author-title::text"),
                'birthdate':extract_width_css(".author-born-date::text"),
               # bio=extract_width_css('.author-description::text')
                })+'\n')

       
           