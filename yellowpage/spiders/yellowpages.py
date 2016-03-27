# -*- coding: utf-8 -*-
import scrapy
from yellowpage.items import YellowpageItem
import re


class GelbeseitenSpider(scrapy.Spider):
    name = "yellowpages"
    allowed_domains = ["http://www.yellowpages.com.au"]

    def start_requests(self):
        # 根据搜索关键字作为入口
        reqs = []
        for i in range(1, 30):
            # hospital
            req_hospital = scrapy.Request('http://www.yellowpages.com.au/search/listings?'
                                 'clue=Hospital&locationClue=All+States&pageNumber=%d' % i)
            # clinic
            req_clinic = scrapy.Request('http://www.yellowpages.com.au/search/listings?'
                                 'clue=clinic&locationClue=All+States&pageNumber=%d' % i)
            # medical equipment
            req_equipment = scrapy.Request('http://www.yellowpages.com.au/search/listings?'
                                 'clue=medical+equipment&locationClue=All+States&pageNumber=%d' % i)

            reqs.append(req_hospital)
            reqs.append(req_clinic)
            reqs.append(req_equipment)

        for i in range(1, 4):
            # medical device
            req_device = scrapy.Request('http://www.yellowpages.com.au/search/listings?'
                                 'clue=medical+device&locationClue=All+States&pageNumber=%d' % i)
            reqs.append(req_device)

        return reqs

    def parse(self, response):
        self.logger.info('parse is running. url is :%s' % response.url)

        div_paths = response.xpath('//*[@id="search-results-page"]/div[1]/div/div[3]/div/div/div[2]/div/div[2]/'
                                   'div[2]/div/div[@class="cell in-area-cell middle-cell"]')
        self.logger.info('div_paths len ::::::::::::::::::::::::: %s' % str(len(div_paths)))
        for div_path in div_paths:
            item = YellowpageItem()
            company_path = div_path.xpath('string(div//a[@class="listing-name"])')
            phone_path = div_path.xpath('div//a[@title="Phone"]/@href')
            email_path = div_path.xpath('div//a[@class="contact contact-main contact-email "]/@href')
            website_path = div_path.xpath('div//a[@class="contact contact-main contact-url "]/@href')

            company = company_path[0].extract() if company_path else ''
            phone_string = phone_path[0].extract() if phone_path else ''
            phone_m = re.match('tel:([0-9]+)', phone_string)
            phone = phone_m.group(1) if phone_m else ''

            email_string = email_path[0].extract() if email_path else ''
            email_m = re.match(r'.*mailto:(.*?)\?subject.*', email_string)
            email = email_m.group(1) if email_m else ''

            website = website_path[0].extract() if website_path else ''

            print 'company :::::::::::::::: ', company
            print 'email   :::::::::::::::: ', email
            print 'phone   :::::::::::::::: ', phone
            print 'website :::::::::::::::: ', website
            item['company'] = company
            item['email'] = email
            item['phone'] = phone
            item['website'] = website

            yield item





















