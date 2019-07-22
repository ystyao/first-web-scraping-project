# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request


class PythonBookSpider(scrapy.Spider):
    #confg
    name = 'python_book'
    allowed_domains = ['amazon.com']
	#urls of the products you like
    start_urls = ['https://www.amazon.com/s?k=python&ref=nb_sb_noss_2']

    def parse(self, response):
        #print(response.url)
        titles = response.xpath('//div[@class="s-result-list s-search-results sg-row"]//div[@class="sg-col-inner"]//h2//span/text()').extract()
        #herfs = response.xpath('//div[@class="s-result-list s-search-results sg-row"]//a[@class="a-link-normal s-faceout-link a-text-normal"]/text()').extract() 
        prices = response.xpath('//div[@class="s-result-list s-search-results sg-row"]//span[@class="a-offscreen"]/text()').extract()
        commits = response.xpath('//div[@class="s-result-list s-search-results sg-row"]//span[@class="a-icon-alt"]/text()').extract()
        total_num = response.xpath('//div[@class="s-result-list s-search-results sg-row"]//span[@class="a-size-small a-color-secondary"]/span/text()').extract()
        #print(total_num)
        for items in zip(titles,prices,commits,total_num):
            yield{
                "title":items[0],
                "priece":items[1],
                "commits":items[2],
                "total_num":items[3]
                }
        next_page = "https://www.amazon.com/" + str(response.xpath('//li[@class="a-last"]/a/@href').extract_first())
        yield Request(next_page)