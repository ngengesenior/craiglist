# -*- coding: utf-8 -*-
import scrapy


class JobsTitleSpider(scrapy.Spider):
    name = 'job_titles'
    # allowed_domains = ['https://newyork.craigslist.org/search/egr']
    start_urls = ["https://newyork.craigslist.org/search/egr/"]

    def parse(self, response):
        titles = response.xpath('//a[@class="result-title hdrlnk"]/text()').extract()
        for title in titles:

            yield {'title': title}
