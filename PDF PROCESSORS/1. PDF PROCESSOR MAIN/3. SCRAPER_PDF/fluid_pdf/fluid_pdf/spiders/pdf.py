# -*- coding: utf-8 -*-
import scrapy
from pathlib import Path
from selenium import webdriver
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from fluid_pdf.items import FluidPdfItem
from selenium.webdriver.common.keys import Keys
from time import sleep
import csv

# prepare a list of links
my_list = []
with open("pdf_links.csv", 'r') as my_file:
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

class PdfSpider(scrapy.Spider):
	name = 'pdf'
	allowed_domains = ['johnsoncontrols.fluidtopics.net']
	start_urls = ['http://johnsoncontrols.fluidtopics.net/']

	def parse(self, response):
		self.driver = webdriver.Chrome(str(Path(Path.cwd(), "chromedriver.exe")), chrome_options=options)
		self.driver.set_window_size(1920, 800)	
		for url in pdf_urls[1000:2000]:
			l = ItemLoader(item=FluidPdfItem(), selector=url)
			self.driver.get(url)
			sleep(1)
			sel = Selector(text=self.driver.page_source)
			try:
				button = self.driver.find_element_by_xpath('//button[contains(@class, "vieweractionsbar-download-button")]')
				button.click()		
				title = sel.xpath('//*[@class="vieweractionsbar-filename"]/span/@title').extract_first()
				link = url		
			except:
				title = "FAILED"
				link = url
				pass		

		
			l.add_value('title', title)
			l.add_value('link', link)
			yield l.load_item()