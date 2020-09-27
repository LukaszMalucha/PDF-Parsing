# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 16:33:18 2020

@author: LukaszMalucha
"""

import spacy
nlp = spacy.load('en_core_web_sm')


with open("peterrabbit.txt") as f:
    doc = nlp(f.read())

    
# For every token in the third sentence, print the token text, the POS tag, the fine-grained TAG tag, and the description of the fine-grained tag.    
    
    
    
    