# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


from scrapy.pipelines.images import ImagesPipeline
import scrapy
import os
from huoHu.settings import IMAGES_STORE as images_store

class HuohuPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        imageUrl = item["v_thumb"]
        realImageUrl = 'http://img.q6pk.com/image'+imageUrl
        return scrapy.Request(realImageUrl)

    def item_completed(self, results, item, info):

        image_path = [x["path"] for ok, x in results if ok]
        print("进来了没有啊", image_path)
        os.rename(images_store+image_path[0], images_store +item["c_id"]+'.jpg')
        return item

