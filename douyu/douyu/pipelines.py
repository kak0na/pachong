# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.images import ImagesPipeline
import os
IMAGES_STORE="D:/work/pacong/douyu/image/"
class DouyuPipeline(ImagesPipeline):

    def get_media_requests(self,item,spider):
        image_link=item['imagelink']
        yield scrapy.Request(image_link)

    def item_completed(self, results, item, info):
        image_path=[x["path"] for ok,x in results if ok ]
        os.rename(IMAGES_STORE+image_path[0],IMAGES_STORE+item["nickname"]+'.jpg')
  #  def process_item(self, item, spider):
  #      return item
