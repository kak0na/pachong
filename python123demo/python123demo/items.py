# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
#这个是管道
import scrapy


class Python123DemoItem(scrapy.Item):
    # define the fields for your item here like:
    #给管道定义名称：类似定义了一个字典一样
    #老师姓名
    name = scrapy.Field()#用这个方法创建了一个字段
    #老师职称
    title= scrapy.Field()
    #老师信息
    info=scrapy.Field()
    pass
