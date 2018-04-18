#!/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2018/4/17 上午9:29
# @Author   :Xiao gang huang
# @File :dmoz_spider.py
import scrapy

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.cocoachina.com/"
        #"http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        #"http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        fileName = response.url.split("/")[-2]
        with open(fileName,'wb') as f:
            f.write(response.body)

        #此处有问题
        #//a[@target="_blank"]/@href
        #//==>
        for sel in response.xpath('//a[@target="_blank"]/@href'):
            title = sel.extract()
            print("targetTitle:",title)
            print("titleInfo:",sel)
