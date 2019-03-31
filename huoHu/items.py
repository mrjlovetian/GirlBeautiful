# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HuohuItem(scrapy.Item):
    c_id = scrapy.Field()
    s_thumb = scrapy.Field()
    h_thumb = scrapy.Field()
    v_thumb = scrapy.Field()

