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

CURRENT_PATH = Path(Path.cwd(), "htmls")
FOLDERS = [str(x) for x in CURRENT_PATH.iterdir() if x.is_dir()]  



def text_extractor():
    """Compiler for html text extraction"""
    for folder in FOLDERS:
        htmls = list(Path(folder).glob('*.html'))
        tables = list(Path(folder, "tables").glob('*.csv'))
        
        for element in tables:
            print(element)
    
    
    
    
    
    
    
    


text_extractor()


def tables_to_dict(filename):
    """Extract csv table data to dictionary"""
    TABLES = list(Path(Path.cwd(),  "htmls", "long", "tables").glob('*.csv'))

    tables_dict = {}
    
    
    for file in TABLES:
        data = []
        with open(str(file), 'r') as csvfile: 
            input_file_name = Path(file).stem
            reader = csv.reader(csvfile, skipinitialspace=True)
            for val in reader:
                data.append(" ".join(val))
        tables_dict[input_file_name] = data       
        

