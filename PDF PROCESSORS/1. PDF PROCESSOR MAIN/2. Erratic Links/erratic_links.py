# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 19:59:01 2020

@author: LukaszMalucha
"""


import pandas as pd


dataset = pd.read_csv("1_documents_merged.csv", encoding='utf-8-sig') 


dataset_missing = pd.read_csv("missing_2.csv", encoding='utf-8-sig') 

dataset_m = dataset_missing['link'].str[39:]


error = dataset[dataset['document_link'] == "/viewer/document/rCIOVzrdjowMs23VSbThYQ"]



"""
REPLACE ERRATIC LINKS
"""

dataset_missing['link'] = dataset_missing['link'].str.replace("/viewer/document/zpLI1JDRBnTwYTyMIczYqg", "/viewer/document/hw6JWFAKzTKFpujvU7eW7g")



# GLAS Smart Thermostat Technical Bulletin PDF REMOVED



















error = dataset[dataset['topic_title'].str.contains("")]