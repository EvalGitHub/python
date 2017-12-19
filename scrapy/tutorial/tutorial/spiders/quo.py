#���� scrapy crawl  author -o au.json

import scrapy
import json

class QuotesSpider(scrapy.Spider):
    name ='author'
    start_urls=['http://quotes.toscrape.com/']
    #û��ʹ��scrapy.Request(url,self.parse)��Ĭ���Զ�ִ��parse�ص�����
    def parse(self,response):
        for href in response.css('.author + a::attr(href)'):
            yield response.follow(href,self.parse_author)

        for href in response.css("li.next a::attr(href)"):
            #response.follow ����ֱ��ʹ�����·��
            yield response.follow(href,self.parse)
            #response.urljoin���Խ����·��ת��Ϊ����·��
            #yield scrapy.Request(response.urljoin(href))

    def parse_author(self,response):
        def extract_width_css(query):
            return response.css(query).extract_first().strip()


        # scrapy crawl author -o au1.json  �������еķ�ʽ��
        yield{
            'name':extract_width_css("h3.author-title::text"),
            'birthdate':extract_width_css(".author-born-date::text"),
           # 'bio':extract_width_css('.author-description::text')
        }
    
        #д���ļ�json.dumps ������ַ���������ֱ�����еķ�ʽ��
        with open("b.json","a") as w:
            w.write(json.dumps({
                'name':extract_width_css("h3.author-title::text"),
                'birthdate':extract_width_css(".author-born-date::text"),
               # bio=extract_width_css('.author-description::text')
                })+'\n')

       
           