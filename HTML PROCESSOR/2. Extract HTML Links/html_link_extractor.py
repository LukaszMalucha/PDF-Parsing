# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 07:57:03 2020

@author: LukaszMalucha
"""

import urllib
import pandas as pd
import requests
import bs4 as bs

dataset = pd.read_csv("htmls_merged.csv", encoding='utf-8-sig')




"""
HTML LINKS DATASET 
"""

dataset = dataset[['document_link']]


dataset = dataset[dataset['document_link'].str.contains('reader')]


dataset['document_link'] = dataset['document_link'].apply(lambda x: "https://johnsoncontrols.fluidtopics.net" + x)


dataset = dataset.drop_duplicates()


dataset.to_csv("links.csv",  encoding='utf-8-sig', index=False)
