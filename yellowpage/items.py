# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YellowpageItem(scrapy.Item):
    # 公司名称
    company = scrapy.Field()
    # 联系电话
    phone = scrapy.Field()
    # 邮箱
    email = scrapy.Field()
    # 公司网站
    website = scrapy.Field()
