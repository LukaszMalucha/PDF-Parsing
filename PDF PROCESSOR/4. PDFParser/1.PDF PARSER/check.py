# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 10:34:23 2020

@author: LukaszMalucha
"""




import pandas as pd


df = pd.read_csv("asd.csv")
df.to_html('asd.html')

from html import HTML
import csv

def to_html(csvfile):
    H = HTML()
    t=H.table(border='2')
    r = t.tr
    with open(csvfile) as csvfile:
        reader = csv.DictReader(csvfile)
        for column in reader.fieldnames:
            r.td(column)
        for row in reader:
            t.tr
            for col in row.iteritems():
                t.td(col[1])
    return t


to