# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HtmlScraperItem(scrapy.Item):
	article_id = scrapy.Field()
	article_txt = scrapy.Field()
	topic_link = scrapy.Field()

