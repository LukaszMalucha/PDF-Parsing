# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 17:21:03 2020

@author: LukaszMalucha
"""

from pathlib import Path
import bs4 as bs
import re
from operator import itemgetter
import itertools
import operator

import csv
import json

CURRENT_PATH = Path(Path.cwd(), "htmls")
FOLDERS = [str(x) for x in CURRENT_PATH.iterdir() if x.is_dir()]  

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
            " | ".join(element)
            element[0] = "TABLE ROW: | " + element[0] + " | "
            sorted_string_list.append(element[0])
        else:
            sorted_string_list.append(element[0])             
        
    return sorted_string_list


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
    pages_dict["Title"] = title                 
    
    return pages_dict    



  

def extract_text(filename):  
    input_file_name = Path(filename).stem
    file_path = Path(Path.cwd(), "htmls", input_file_name, filename)
    
    # Turn html into bs.soup
    soup = bs.BeautifulSoup(open(str(file_path)), "lxml")
    
    pages = document_pages(soup)
    pages_text = text_per_page(soup, pages)
    
    # Save data as json
    output_txt_path = Path(Path.cwd() ,"text")
    output_txt_path.mkdir(parents=True, exist_ok=True) 
    text_file_path = Path(output_txt_path,  input_file_name + ".json")    
    with open(text_file_path, 'w') as fp:
        json.dump(pages_text, fp)
        
    
    return pages_text

extract_text("long.html")

def text_extractor():
    """Compiler for html text extraction"""
    for folder in FOLDERS:
        htmls = list(Path(folder).glob('*.html'))
        tables = list(Path(folder, "tables").glob('*.csv'))
        
        for element in htmls:
            extract_text(str(element))

        


text_extractor()














#
#
#def tables_to_dict(filename):
#    """Extract csv table data to dictionary"""
#    TABLES = list(Path(Path.cwd(),  "htmls", "long", "tables").glob('*.csv'))
#
#    tables_dict = {}
#    
#    
#    for file in TABLES:
#        data = []
#        with open(str(file), 'r') as csvfile: 
#            input_file_name = Path(file).stem
#            reader = csv.reader(csvfile, skipinitialspace=True)
#            for val in reader:
#                data.append(" ".join(val))
#        tables_dict[input_file_name] = data       
        

