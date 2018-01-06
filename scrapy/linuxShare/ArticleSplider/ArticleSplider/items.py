# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

import datetime
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose,TakeFirst,Join

import re

class ArticlespliderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


def add_jobbole(value):
    return value+"-jobbole"


def date_convert(value):
    try:
        create_date = datetime.datetime.strptime(value, "%Y/%m/%d").date()
    except Exception as e:
        create_date = datetime.datetime.now().date()

    return create_date


def get_nums(value):
    match_re = re.match(".*(\d+).*", value)
    if match_re:
        nums = int(match_re.group(1))
    else:
        nums = 0
    return nums


def remove_comment_tags(value):
    #去掉tag中提取的评论
    if "评论" in value:
        return " "
    else:
        return value


def return_value(value):
    return value


class ArticleItemLoader(ItemLoader):
    default_output_processor=TakeFirst()


class JobBoleArticleitem(scrapy.Item):
    title =scrapy.Field(
        #input_processor=MapCompose(add_jobbole)
        #mapcompose 用于预处理
        input_processor = MapCompose(lambda x:x+"-jobbole",add_jobbole)
    )
    create_date= scrapy.Field(
        input_processor =MapCompose(date_convert),
        #取第一个
       # output_processor=TakeFirst()
    )
    url=scrapy.Field()
    url_obj_id=scrapy.Field()
    font_image_url=scrapy.Field(
        output_processor=MapCompose(return_value),
    )
    font_image_path=scrapy.Field()
    praise_nums=scrapy.Field(
        input_processor=MapCompose(get_nums),
    )
    comment_nums=scrapy.Field(
        input_processor=MapCompose(get_nums),
    )
    fav_nums=scrapy.Field(
        input_processor=MapCompose(get_nums),
    )
    tags=scrapy.Field(
        input_processor = MapCompose(remove_comment_tags),
        output_processor=Join(","),
    )
    content=scrapy.Field()

