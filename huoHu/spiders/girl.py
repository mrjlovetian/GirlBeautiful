# -*- coding: utf-8 -*-
import scrapy
import json
from huoHu.items import HuohuItem

class GirlSpider(scrapy.Spider):
    name = 'girl'
    allowed_domains = ['tubaxian.com']
    index = 1
    base_url = 'http://api12.tubaxian.com/api/content/contentList?type=2&page='
    start_urls = [base_url + str(index)]

    def parse(self, response):
        girl_data = json.loads(response.body)['data']['info_list']
        for dic in girl_data:
            item = HuohuItem()
            item['c_id'] = dic['id']
            item['s_thumb'] = dic['s_thumb']
            item['h_thumb'] = dic['h_thumb']
            item['v_thumb'] = dic['v_thumb']
            yield item

        if len(girl_data) != 0:
            self.index += 1
            yield scrapy.Request(self.base_url + str(self.index), callback=self.parse)