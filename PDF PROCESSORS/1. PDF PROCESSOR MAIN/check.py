# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 19:59:01 2020

@author: LukaszMalucha
"""


import pandas as pd


dataset = pd.read_csv("9_documents_fixed_topics.csv", encoding='utf-8-sig') 


dataset_missing = pd.read_csv("missing_2.csv", encoding='utf-8-sig') 
missing_list = dataset_missing['link'].to_list()



error = dataset[dataset['document_link'] == "/viewer/document/~szOCIHYB9h_hB4TfDrrdQ"]

error = dataset[dataset['topic_title'].str.contains("Thermostat Modbus")]