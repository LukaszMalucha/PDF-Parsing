# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 07:57:03 2020

@author: LukaszMalucha
"""


import pandas as pd



dataset = pd.read_csv("1_documents_merged.csv", encoding='utf-8-sig')




"""
PDF LINKS DATASET 
"""

dataset = dataset[['document_link']]


dataset = dataset[dataset['document_link'].str.contains('viewer')]


dataset['document_link'] = dataset['document_link'].apply(lambda x: "https://johnsoncontrols.fluidtopics.net" + x)


dataset = dataset.drop_duplicates()


dataset.to_csv("pdf_links.csv",  encoding='utf-8-sig', index=False)



