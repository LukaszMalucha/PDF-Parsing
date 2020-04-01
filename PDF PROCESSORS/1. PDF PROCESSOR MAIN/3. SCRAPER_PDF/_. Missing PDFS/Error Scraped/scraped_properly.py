# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 10:30:13 2020

@author: LukaszMalucha
"""

# -*- coding: utf-8 -*-

from pathlib import Path
import pandas as pd


# Folder Paths
PDFS = list(Path(Path.cwd()).glob('*.pdf'))

pdf_list = []
for element in PDFS:
    file_name = Path(element).stem
    pdf_list.append(file_name + ".pdf")
    
    
dataset_scraped = pd.DataFrame({"title": pdf_list})    



dataset_full = pd.read_csv("pdfs.csv", encoding='utf-8-sig')

#dataset_full = dataset_full[['title']]


dataset = dataset_full[~dataset_full['title'].isin(pdf_list)]



missing = dataset[dataset['title']!="FAILED"]

missing = missing[['link']]

missing.to_csv("error_scraped.csv",  encoding='utf-8-sig', index=False) 




