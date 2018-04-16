#!/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2018/4/16 上午11:01
# @Author   :Xiao gang huang
# @File :BDItem.py

import scrapy


class BDItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    des = scrapy.Field()
