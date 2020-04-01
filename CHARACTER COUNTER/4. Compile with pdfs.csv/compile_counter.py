# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 16:03:37 2020

@author: LukaszMalucha
"""

import pandas as pd




def match_document(string, doc_lst):
    if string == doc_lst[0]:
        new_string = doc_lst[1]
        return new_string
    
    
dataset_pdfs = pd.read_csv("pdfs.csv", encoding="utf-8")    
dataset_pdfs['title'] = dataset_pdfs['title'].str.replace("PDF", "pdf")

dataset_counter = pd.read_csv("counter_dataset.csv", encoding="utf-8")



merged_dataset = (pd.merge(dataset_pdfs, dataset_counter, on = "title", how='left').fillna("NONE"))

merged_dataset.to_csv("documents_with_counters.csv", encoding='utf-8', index=False) 