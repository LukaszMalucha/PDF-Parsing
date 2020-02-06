# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 14:32:58 2020

@author: LukaszMalucha
"""


from pathlib import Path
import bs4 as bs
import re
from operator import itemgetter


file_path = Path(Path.cwd(), "long.html")



def extract_text(filename):
    
    soup = bs.BeautifulSoup(open(str(file_path)), "lxml")
    
    # Get all divs and page frames
    divs = [ data for data in soup.select('div') if 'top' in str(data)]
    page_frames = [ data for data in soup.select('div') if "<a name=" in str(data)] 
    
    
    # Get Page count and page frames 
    pages= []
    for count,page in enumerate(page_frames):
        tup = ()
        top = int(re.search(r'(?is)(top:)(.*?)(px)',str(page.get('style'))).group(2))
        bottom = top + 842
        tup = (count+1, top, bottom)
        pages.append(tup)
    
    # Get all the text per page
    pages_dict = dict() 
    header_spans = []
    for page in pages:
        page_text = []  
        for div in divs: 
            page_location = re.search(r'(?is)(top:)(.*?)(px)',str(div.get('style'))).group(2)
            
            # Get a header area to identify potential title
            if int(page_location) < 285:
                spans = [ data for data in div.select('span') if 'font-size' in str(data)]
                for span in spans:
                    tup = ()
                    font_size = re.search(r'(?is)(font-size:)(.*?)(px)',str(span.get('style'))).group(2)
                    tup = (str(span.text).strip(), int(font_size.strip()))
                    header_spans.append(tup)
            
            # Sort text by page
            if page[1] < int(page_location) < page[2]:
                page_text.append(str(div.text).strip())
                     
        pages_dict["Page " + str(page[0])] = page_text
        
    # Get title - from page 1 top (Height: 842px --> up to 285px roughly 33%)   
    title = max(header_spans,key=itemgetter(1))[0]    # biggest font in a header
    pages_dict["Page 1"].remove(title) # Remove first matching element
    
    pages_dict["Title"] = title    
    
    
    return pages_dict

text = extract_text(file_path)

    


    
    
    
    
    
    
















