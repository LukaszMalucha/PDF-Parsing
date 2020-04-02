# -*- coding: utf-8 -*-
import scrapy
from pathlib import Path
from selenium import webdriver
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from html_scraper.items import HtmlScraperItem
from selenium.webdriver.common.keys import Keys
from time import sleep
import csv
import w3lib.html
import re

# prepare a list of links
my_list = []
with open("htmls_merged.csv", 'r') as my_file:
	reader = csv.reader(my_file, delimiter='\t')
	next(reader)
	
	my_list = list(reader)
	
pdf_urls = []
for sublist in my_list:
	for item in sublist:
		pdf_urls.append(item)



## AVOID HANDSHAKE ERRORS
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')

class HtmlSpider(scrapy.Spider):
	name = 'html'
	allowed_domains = ['johnsoncontrols.fluidtopics.net']
	start_urls = ['http://johnsoncontrols.fluidtopics.net/']

	def parse(self, response):
		self.driver = webdriver.Chrome(str(Path(Path.cwd(), "chromedriver.exe")), chrome_options=options)
		self.driver.set_window_size(1920, 800)	
		for url in pdf_urls[:1]:
			
			self.driver.get(url)
			sleep(5)
			sel = Selector(text=self.driver.page_source)	
			section = sel.xpath('//section')	
			articles = section.xpath('//article[contains(@class, "readercontent-loaded")]')
			for article in articles:
				l = ItemLoader(item=HtmlScraperItem(), selector=article)
				try:					
					article_id = article.xpath('.//@id').extract_first()
					article_txt = w3lib.html.remove_tags(article.extract())
					article_txt = article_txt.replace("\n", " ")
					article_txt = re.sub(r'[\W_]+', '', article_txt)

					l.add_value('article_id', article_id)
					l.add_value('article_txt', article_txt)
					l.add_value('topic_link', url)
					yield l.load_item()
				except:
					l.add_value('article_id', "FAILED")
					l.add_value('article_txt', "FAILED")
					l.add_value('topic_link', "FAILED")
					yield l.load_item()		

				



# driver.get("https://johnsoncontrols.fluidtopics.net/reader/wfPqo8iG7TbH~yEr8v82aw/root")
# sel = Selector(text=driver.page_source)
# section = sel.xpath('//section')
# articles = section.xpath('//article[contains(@class, "readercontent-loaded")]')
# article_id = section.xpath('//article[contains(@class, "readercontent-topic")]/@id')[1].extract()
# article = section.xpath('//article[contains(@class, "readercontent-loaded")]')[1]
# article_section = article('.//*section')


# for article in articles:
# 	article_id = article.xpath('.//@id').extract_first()
# 	article_txt = w3lib.html.remove_tags(article.extract())
# 	print(article_id)
















