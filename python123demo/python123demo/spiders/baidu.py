# -*- coding: utf-8 -*-
#设置utf-8编码------>传失败了
#import sys
#reload(sys)
#sys.setdefaultencoding("utf-8")

import scrapy
from python123demo.items import Python123DemoItem

class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['www.itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        node_list=response.xpath("//div[@class='li_txt']")  #xpath 会返回列表
   #     items=[]
        for node in node_list:
            item=Python123DemoItem()
            name=node.xpath("./h3/text()").extract()    #xpath是个列表   xpath是个对象，要用extract提取内容并是unicode编码
            title=node.xpath("./h4/text()").extract()
            info= node.xpath("./p/text()").extract()
            item['name']=name[0]
            item['title']=title[0]
            item['info']=info[0]
    #        items.append(item)
            print(item)
            return item
      #  return items #返回的是列表，所以直接返回给 引擎    如果返回items的字段（Python123DemoItem）就直接返回给pipelines.py（管道