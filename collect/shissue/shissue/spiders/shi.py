from numpy import newaxis
import scrapy
# import datetime
import time
import random


class ShiSpider(scrapy.Spider):
    name = 'shi'
    allowed_domains = ['https://www.shanghai.gov.cn']

    # def url_gen(self):
    #     start_date = datetime.date(2022, 5, 13)
    #     end_date   = datetime.date(2022, 5, 14)
    #     delta_date = datetime.timedelta(days=1)
   
    #     yield start_date.strftime("%Y%m%d")
    #     print('Now yielding ', start_date.strftime("%Y%m%d"))

    #     while start_date <= end_date:
    #         start_date += delta_date
    #         yield start_date.strftime("%Y%m%d")
    #         print('Now yielding ', start_date.strftime("%Y%m%d"))

    def url_gen(self):
        start_page = 5
        end_page = 5

        while start_page <= end_page:
            yield start_page
            start_page += 1


    def start_requests(self):
        # urls = [
#             'https://quotes.toscrape.com/page/1/',
#             'https://quotes.toscrape.com/page/2/',
            #   'https://quotes.toscrape.com/'
        # ]
        # for url in urls:
            # yield scrapy.Request(url=url, callback=self.parse)
        
        url_base = 'https://www.shanghai.gov.cn/nw4411/index_'

        for item in self.url_gen():
            url = url_base + str(item) + '.html'
            time.sleep(random.randint(3,5))
            print('dealing with ',  url)
            yield scrapy.Request(url=url, callback=self.parse_links)

    def parse_links(self, response):
        # filename = f'quotes-test.html'
        # filename = f'quotes-testtt.html'
        # with open(filename, 'a') as f:
            # total content
            # content = response.body

            # all the links to the daily news 
            # content = response.xpath('//a[contains(@href, "/nw4411/")]/@href').extract()
            # for i in content:
            #     f.write(str(i) + '\n')
            # f.write('new page!!!!!!\n')


        # enter on of  the daily news
        # link = 'https://www.shanghai.gov.cn' + links[2]
        # print('link', link)
        # yield scrapy.Request(url=link, callback=self.parse_content, dont_filter = True)
        # time.sleep(random.randint(1,2))

        # enter all the daily news 
        links = response.xpath('//a[contains(@href, "/nw4411/20")]/@href').extract()
        for link in links[4:6]:
            link = 'https://www.shanghai.gov.cn' + link
            print('link', link)
            yield scrapy.Request(url=link, callback=self.parse_content, dont_filter = True)
            time.sleep(random.randint(1,2))




    def parse_content(self, response):
        # filename = f'quotes-test_3.html'
        filename = f'quotes-test_4.html'
        with open(filename, 'a') as f:
            # f.write(response.body)
            title   = response.xpath('//h2[contains(@class, "Article-title")]/text()').extract()
            date    = response.xpath('//small[contains(@class, "Article-time")]/text()').extract()
            source  = response.xpath('//small[contains(@class, "Article-time")]/span/text()').extract()
            shit    = response.xpath('//div[contains(@class, "Article_content")]/div/p/text()').extract()
            
            print('title', title[0])
            print('date', date[0])
            print('source', source[0])
            print('author', shit[0])
            print('shit', shit[1:])

 

        
