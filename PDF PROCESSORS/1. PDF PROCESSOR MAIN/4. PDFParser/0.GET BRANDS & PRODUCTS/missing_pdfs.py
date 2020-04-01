# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 16:56:24 2020

@author: LukaszMalucha
"""


import pandas as pd
import numpy as np



dataset_brands = pd.read_csv("9_documents_fixed_topics.csv", encoding='utf-8-sig') 
dataset_brands = dataset_brands[['document_link', 'brand', 'product_name']]

brands = list(dataset_brands['brand'].unique())



dataset_pdfs = pd.read_csv("pdfs.csv", encoding='utf-8-sig')

dataset_pdfs['document_link'] = dataset_pdfs['link'].str[39:]
dataset_pdfs = dataset_pdfs[dataset_pdfs['title'] != 'FAILED']


dataset_pdfs = dataset_pdfs[['document_link', 'title' ]]


tuples = [tuple(x) for x in dataset_brands.to_numpy()]




def add_brands(string, tuples):
    for element in tuples:
        if string == element[0]:
            brand = element[1]

            
            return brand
        
def add_products(string, tuples):
    for element in tuples:
        if string == element[0]:
            product = element[2]
            product = product.replace(" ", "_")     
            product = product.replace("/", "_")
            return product        
        

dataset_pdfs['brand'] = dataset_pdfs['document_link'].apply(lambda x: add_brands(x, tuples))  
dataset_pdfs['product'] = dataset_pdfs['document_link'].apply(lambda x: add_products(x, tuples)) 
dataset_pdfs = dataset_pdfs[['brand','title', 'product']]     
dataset_pdfs['title'] = dataset_pdfs['title'].str.replace(".pdf", "")

dataset_pdfs = dataset_pdfs.replace(to_replace='None', value=np.nan).dropna()

  
#dataset_pdfs['pdf_name'] = dataset_pdfs[dataset_pdfs.columns[0:]].apply(lambda x: '-'.join(x.dropna().astype(str)), axis=1)    
    




dataset_pdfs.to_csv("pdf_brand_names.csv",  encoding='utf-8-sig', index=False) 