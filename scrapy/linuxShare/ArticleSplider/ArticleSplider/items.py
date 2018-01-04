# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ArticlespliderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class JobBoleArticleitem(scrapy.Item):
    title =scrapy.Field()
    create_date= scrapy.Field()
    url=scrapy.Field()
    url_obj_id=scrapy.Field()
    font_image_url=scrapy.Field()
    font_image_path=scrapy.Field()
    praise_nums=scrapy.Field()
    comment_nums=scrapy.Field()
    fav_nums=scrapy.Field()
    tags=scrapy.Field()
    content=scrapy.Field()

