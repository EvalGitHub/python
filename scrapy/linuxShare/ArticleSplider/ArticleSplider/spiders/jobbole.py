# -*- coding: utf-8 -*-
import scrapy
import re


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/113367/']

    def parse(self, response):
        title = response.xpath("//div[@class='entry-header']/h1/text()").extract_first("no data no data")
        print(title)
        create_date = response.xpath("//p[@class='entry-meta-hide-on-mobile']/text()").extract()[0].strip().replace("·",
                                                                                                                    "")
        parse = int(response.xpath('//span[contains(@class,"vote-post-up")]/h10/text()').extract()[0])

        fav_nums = response.xpath('//span[contains(@class," bookmark-btn")]/text()').extract()[0]
        match_re = re.match(".*(\d+).*", fav_nums)
        if match_re:
            fav_nums = match_re.group(1)

        comment_num = response.xpath('//a[@href="#article-comment"]/span/text()').extract()[0]
        match_com_re = re.match(".*(\d+).*", comment_num)
        if match_com_re:
            comment_num = match_com_re.group(1)

        content = response.xpath('//div[@class="entry"]').extract()[0]

        # tag
        tag_list = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/a/text()').extract()
        tag_list = [element for element in tag_list if not element.strip().endswith("评论")]
        tags = ",".join(tag_list)

#------------------- 通过css选择器提取字段---------------------------------
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

        pass
