# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request


class JobMultipleSpider(scrapy.Spider):
    name = 'job_all'
    # allowed_domains = ['https://newyork.craigslist.org/search/egr']
    start_urls = ["https://newyork.craigslist.org/search/egr/"]

    def parse(self, response):
        jobs = response.xpath('//p[@class="result-info"]')
        for job in jobs:
            title = job.xpath('a/text()').extract_first()
            address = job.xpath('span[@class="result-meta"]/span[@class="result-hood"]/text()').extract_first()
            relative_url = job.xpath('a/@href').extract_first()
            absolute_url = response.urljoin(relative_url)
            meta = {'URL': absolute_url, 'Title': title, 'Address': address}
            """
            At this stage, do not yield the data yet, but we want you to open
            the link to the current craiglist job and scrape the details using the
            `parse_page` function
            """
            yield Request(absolute_url, callback=self.parse_page, meta=meta)

        relative_next_url = response.xpath('//a[@class="button next"]/@href').extract_first()
        absolute_next_url = response.urljoin(relative_next_url)
        yield Request(absolute_next_url, self.parse)

    def parse_page(self, response):
        description = response.xpath('//*[@id="postingbody"]/text()').extract()
        # Now add the description key,value to the meta dict from previous function call
        response.meta['description'] = description
        yield response.meta
