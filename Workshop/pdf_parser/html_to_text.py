# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 13:05:56 2020

@author: LukaszMalucha
"""

from pathlib import Path
import bs4 as bs
import re
from operator import itemgetter
import itertools
import operator

import csv

def sort_strings(l):
    """Group strings by their page location in order to keep row together"""
    sorted_strings = {}
    for string in l:
        if string[0] not in sorted_strings:
            sorted_strings[string[0]] = []
        sorted_strings[string[0]].append(string[1]) 
               
    
    sorted_values = sorted(sorted_strings.items(), key=operator.itemgetter(0))
    
    sorts = []
    for element in sorted_values:
        sorts.append(list(reversed(element[1]))) 
        
        
    # REMOVE TABLE STRINGS AND REPLACE THEM WITH "TABLE ROW" Message
    sorted_string_list = []     
    for element in sorts:
        if len(element) > 1:
            sorted_string_list.append("TABLE ROW")
        else:
            sorted_string_list.append(element[0])             
        
    return sorted_string_list


data = []

with open('long.csv', 'r') as csvfile: 
    reader = csv.reader(csvfile, skipinitialspace=True)
    for val in reader:
        data.append(" ".join(val))






# Get Page count and page frames 

def document_pages(soup):
    """Get Page count and page frames in order to sort strings by page"""
    page_frames = [ data for data in soup.select('div') if "<a name=" in str(data)]    
    
    pages_list= []
    for count,page in enumerate(page_frames):
        tup = ()
        top = int(re.search(r'(?is)(top:)(.*?)(px)',str(page.get('style'))).group(2))
        bottom = top + 842
        tup = (count+1, top, bottom)
        pages_list.append(tup)
    
    return pages_list    
        
    


def text_per_page(soup, pages):
    """Return dictionary of {page<n> : "[ Strings per page n ]"} """    
    pages_dict = dict() 
    header_spans = []
    
    divs = [ data for data in soup.select('div') if 'top' in str(data)]
    
    for page in pages:
        page_text = []  
        for div in divs:
            page_location = re.search(r'(?is)(top:)(.*?)(px)',str(div.get('style'))).group(2)
            
            # Get a header area to identify potential title(between 0 - 285px, roughly 33%)            
            if int(page_location) < 285:
                spans = [ data for data in div.select('span') if 'font-size' in str(data)]
                for span in spans:
                    font_size = re.search(r'(?is)(font-size:)(.*?)(px)',str(span.get('style'))).group(2)
                    tup = [str(span.text).strip(), int(font_size.strip())]
                    header_spans.append(tup)
        
            # Sort text by page
            if page[1] < int(page_location) < page[2]:
                page_text.append((int(page_location), str(div.text).strip()))
                
                  
        page_text_sorted = sort_strings(page_text)
        pages_dict["Page " + str(page[0])] = page_text_sorted
    title = max(header_spans,key=itemgetter(1))[0]    # biggest font in a header 
    pages_dict["Page 1"].remove(title) # Remove first matching element to avoid duplicate title
    pages_dict["Title"] = title                 
    
    return pages_dict    



  

def extract_text(filename):
    file_path = Path(Path.cwd(), filename)
    
    # Turn html into bs.soup
    soup = bs.BeautifulSoup(open(str(file_path)), "lxml")
    
    pages = document_pages(soup)
    pages_text = text_per_page(soup, pages)
    
    return pages_text
    


final = extract_text("long.html")











    
    
    
    
















