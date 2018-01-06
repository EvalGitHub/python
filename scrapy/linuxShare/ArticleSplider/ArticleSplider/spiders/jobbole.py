# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.http import Request

# 绝对url 与相对url
from urllib import parse

import datetime

from  ArticleSplider.items import JobBoleArticleitem,ArticleItemLoader


from ArticleSplider.utils.common import get_md5

from scrapy.loader import ItemLoader

class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts/']

    def parse(self, response):
        '''
        1)获取文章列表的url,并交给scrapy 下载后并进行解析
        2）获取下一页的url 并交给scrapy进行下载，下载完成后交给parse
        '''
        # 解析列表中的所有文章url 并交给scrapy下载后并进行解析
        post_nodes = response.css("#archive .floated-thumb .post-thumb a")
        for post_node in post_nodes:
            # parse.urljoin(response.url,post_url)会主动将第一个url的域名取出来，加上后面的url
            image_url = post_node.css("img::attr(src)").extract_first("")
            post_url = post_node.css("::attr(href)").extract_first("")

            #meta 用于向response中添加值
            yield Request(url=parse.urljoin(response.url, post_url), meta={"font_image_url":image_url},callback=self.parse_detail)


        # 提取下一页，进行解析
        next_url = response.css(".next.page-numbers::attr(href)").extract_first("没有下一个url")
        if next_url:
            yield Request(url=parse.urljoin(response.url, post_url), callback=self.parse)


    def parse_detail(self, response):

        article_item=JobBoleArticleitem()

        # 提取文章的具体字段
        '''
        font_image_url=response.meta.get("font_image_url","")#文章封面图
        title = response.xpath("//div[@class='entry-header']/h1/text()").extract_first("no data no data")
        create_date = response.xpath("//p[@class='entry-meta-hide-on-mobile']/text()").extract()[0].strip().replace("·",
                                                                                                                    "")
        praise_nums = int(response.xpath('//span[contains(@class,"vote-post-up")]/h10/text()').extract()[0])

        fav_nums = response.xpath('//span[contains(@class," bookmark-btn")]/text()').extract()[0]
        match_re = re.match(".*(\d+).*", fav_nums)
        if match_re:
            fav_nums = int(match_re.group(1))
        else:
            fav_nums = 0

        comment_nums = response.xpath('//a[@href="#article-comment"]/span/text()').extract()[0]
        match_com_re = re.match(".*(\d+).*", comment_nums)
        if match_com_re:
            comment_nums = int(match_com_re.group(1))
        else:
            comment_nums = 0
        content = response.xpath('//div[@class="entry"]').extract()[0]

        # tag
        tag_list = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/a/text()').extract()
        tag_list = [element for element in tag_list if not element.strip().endswith("评论")]
        tags = ",".join(tag_list)
        '''



        # ------------------- 通过css选择器提取字段---------------------------------
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
        '''
        
        article_item["url_obj_id"] = get_md5(response.url)
        article_item["title"]   =title

        article_item["url"]=response.url
       #article_item["url_obj_id"]=

        try:
            create_date =datetime.datetime.strptime(create_date,"%Y/%m/%d").date()
        except Exception as e:
            create_date=datetime.datetime.now().date()

        article_item["create_date"] = create_date

        article_item["font_image_url"]= [font_image_url]
      #  article_item["font_image_path"]=
        article_item["praise_nums"]=praise_nums
        article_item["comment_nums"]=comment_nums
        article_item["fav_nums"]=fav_nums
        article_item["tags"]=tags
        article_item["content"]=content

        '''


#通过item_loader 加载item
        font_image_url = response.meta.get("font_image_url", "")  # 文章封面图
        item_loader = ArticleItemLoader(item=JobBoleArticleitem(),response=response)
        item_loader.add_css("title",".entry-header h1::text")
      #  item_loader.add_xpath()
        item_loader.add_value("url",response.url)
        item_loader.add_value("url_obj_id",get_md5(response.url))
        item_loader.add_css("create_date","p.entry-meta-hide-on-mobile::text")
        item_loader.add_value("font_image_url",[font_image_url])
        item_loader.add_css("praise_nums",".vote-post-up h10::text")
        item_loader.add_css("comment_nums","a[href='#article-comment'] span::text")
        item_loader.add_css("fav_nums",".bookmark-btn::text")
        item_loader.add_css("tags","p.entry-meta-hide-on-mobile a::text")
        item_loader.add_css("content","div.entry")


        article_item=item_loader.load_item()

        yield article_item
