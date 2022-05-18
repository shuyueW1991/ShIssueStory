from numpy import newaxis
import scrapy
# import datetime
import time
import random

from shissue.items import ShissueItem


class ShiSpider(scrapy.Spider):
    name = 'shi'
    allowed_domains = ['https://www.shanghai.gov.cn']

    def url_gen(self):
        start_page = 2
        end_page = 21

        while start_page <= end_page:
            yield start_page
            start_page += 1


    def start_requests(self):
        url_base = 'https://www.shanghai.gov.cn/nw4411/index_'

        for item in self.url_gen():
            url = url_base + str(item) + '.html'
            time.sleep(random.randint(3,5))
            print('dealing with ',  url)
            yield scrapy.Request(url=url, callback=self.parse_links)

    def parse_links(self, response):
        # enter all the daily news 
        links = response.xpath('//a[contains(@href, "/nw4411/20")]/@href').extract()
        for link in links:
            link = 'https://www.shanghai.gov.cn' + link
            print('link', link)
            yield scrapy.Request(url=link, callback=self.parse_content, dont_filter = True)
            time.sleep(random.randint(1,2))


    def parse_content(self, response):
        # filename = f'quotes-test_4.html'
        # with open(filename, 'a') as f:
            # f.write(response.body)

        title   = response.xpath('//h2[contains(@class, "Article-title")]/text()').extract()
        date    = response.xpath('//small[contains(@class, "Article-time")]/text()').extract()
        source  = response.xpath('//small[contains(@class, "Article-time")]/span/text()').extract()
        # author  = response.xpath('//div[contains(@class, "Article_content")]/div/p[1]/text()').extract()
        shit    = response.xpath('//div[contains(@class, "Article_content")]/div/p/text()').extract()
        
        item = ShissueItem()
        item['title'] =  title[0].strip().strip("\n")
        item['date']  =  date[0].strip().strip("\n")
        item['source'] = source[0].strip("来源：").strip("  ").strip().strip("\n")
        item['author'] = shit[0].strip("  ").strip().strip("\n")
        item['text'] = shit[1].strip("  ").strip("\u2003\u2003").strip().strip("\n")
        for i in range(2, len(shit)):
            item['text'] += shit[i].strip("  ").strip("\u2003\u2003").strip().strip("\n")

        # print('title', item['title'])
        # print('date', item['date'])
        # print('source', item['source'])
        # print('author', item['author'])
        # print('text', item['text'])
        yield item

 