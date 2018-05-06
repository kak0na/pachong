# -*- coding: utf-8 -*-
import scrapy
import json
from douyu.items import DouyuItem
class DouyuSpider(scrapy.Spider):
    name = 'Douyu'
    allowed_domains = ['capi.douyucdn.cn']
    baseurl='http://capi.douyucdn.cn/api/v1/getverticalroom?limit=20000&offser=40'
    offser=''
    start_urls = [baseurl+str(offser)]
    def parse(self, response):
        data_list=json.loads(response.body)['data']
        for data in data_list:
            item=DouyuItem()
            item['nickname']=data['nickname']
            item['imagelink']=data['vertical_src']
            yield item
