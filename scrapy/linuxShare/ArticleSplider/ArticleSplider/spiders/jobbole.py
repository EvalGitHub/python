# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.http import Request

#绝对url 与相对url
from urllib import parse

class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts/']


    def parse(self, response):
        '''
        1)获取文章列表的url,并交给scrapy 下载后并进行解析
        2）获取下一页的url 并交给scrapy进行下载，下载完成后交给parse
        '''
        #解析列表中的所有文章url 并交给scrapy下载后并进行解析
        post_urls=response.css("#archive .floated-thumb .post-thumb a::attr(href)").extract()
        for post_url in post_urls:
            #parse.urljoin(response.url,post_url)会主动将第一个url的域名取出来，加上后面的url
           yield Request(url=parse.urljoin(response.url,post_url),callback=self.parse_detail)

        #提取下一页，进行解析
        next_url=response.css(".next.page-numbers::attr(href)").extract_first("没有下一个url")
        if next_url:
            yield Request(url=parse.urljoin(response.url, post_url), callback=self.parse)


    def parse_detail(self,response):
        #提取文章的具体字段
        title = response.xpath("//div[@class='entry-header']/h1/text()").extract_first("no data no data")
        create_date = response.xpath("//p[@class='entry-meta-hide-on-mobile']/text()").extract()[0].strip().replace("·",
                                                                                                                    "")
        parse = int(response.xpath('//span[contains(@class,"vote-post-up")]/h10/text()').extract()[0])

        fav_nums = response.xpath('//span[contains(@class," bookmark-btn")]/text()').extract()[0]
        match_re = re.match(".*(\d+).*", fav_nums)
        if match_re:
            fav_nums = int(match_re.group(1))
        else:
            fav_nums=0

        comment_num = response.xpath('//a[@href="#article-comment"]/span/text()').extract()[0]
        match_com_re = re.match(".*(\d+).*", comment_num)
        if match_com_re:
            comment_num = int(match_com_re.group(1))
        else:
            comment_num=0
        content = response.xpath('//div[@class="entry"]').extract()[0]

        # tag
        tag_list = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/a/text()').extract()
        tag_list = [element for element in tag_list if not element.strip().endswith("评论")]
        tags = ",".join(tag_list)

#------------------- 通过css选择器提取字段---------------------------------
        '''
        title = response.css(".entry-header h1::text").extract()
        create_date = response.css("p.entry-meta-hide-on-mobile::text").extract()[0].strip().replace("·", "")

        fav_nums = response.css(".bookmark-btn::text").extract()[0]
        match_re = re.match(".*(\d+).*", fav_nums)
        if match_re:
            fav_nums = match_re.group(1)

        comment_num=response.css("a[href='#article-comment'] span::text").extract()[0]
        match_com_re = re.match(".*(\d+).*", comment_num)
        if match_com_re:
            comment_num = match_com_re.group(1)

        content=response.css("div.entry").extract()[0]
        tags=response.css("p.entry-meta-hide-on-mobile a::text").extract()[0]
        
        '''


        pass
