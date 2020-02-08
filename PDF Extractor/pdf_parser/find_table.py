# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 17:43:55 2020

@author: LukaszMalucha
"""

from pathlib import Path
import bs4 as bs
import re
from operator import itemgetter


file_path = Path(Path.cwd(), "long.html")


soup = bs.BeautifulSoup(open(str(file_path)), "lxml")


border_spans = [ data for data in soup.select('span') if 'height:0px;' and data.text == "" in str(data)]
    
page_location_list = []

    
for element in border_spans:
    
    page_location = re.search(r'(?is)(top:)(.*?)(px)',str(element.get('style'))).group(2)
    element_width = re.search(r'(?is)(width:)(.*?)(px)',str(element.get('style'))).group(2)
    if 842 < int(page_location) < 1842 and int(element_width) == 0:
        page_location_list.append(int(page_location))
        
      
        
top = min(page_location_list)        
bottom = max(page_location_list)




text_divs = [ data for data in soup.select('div') if 'font-size' in str(data) and "top:" in str(data)]

for element in text_divs:
    page_location = re.search(r'(?is)(top:)(.*?)(px)',str(element.get('style'))).group(2)
    
    if top < int(page_location) < bottom:
        print(element.text)
    
