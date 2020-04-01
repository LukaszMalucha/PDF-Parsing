# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 16:56:24 2020

@author: LukaszMalucha
"""


from pathlib import Path
import pandas as pd



dataset_scraped = pd.read_csv("pdfs.csv", encoding='utf-8-sig') 


dataset_scraped = dataset_scraped[dataset_scraped['title'].notna()]
dataset_scraped = dataset_scraped[dataset_scraped['title'] != 'FAILED']
dataset_scraped = dataset_scraped[['link']]


dataset_full = pd.read_csv("pdf_links.csv", encoding='utf-8-sig')
dataset_full['link'] = dataset_full['document_link']
dataset_full = dataset_full[['link']]



common = dataset_full.merge(dataset_scraped,on=['link'])


missing = dataset_full[(~dataset_full.link.isin(common.link))]

missing.to_csv("missing_2.csv",  encoding='utf-8-sig', index=False) 