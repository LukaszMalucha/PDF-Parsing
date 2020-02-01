# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 09:46:47 2020

@author: LukaszMalucha
"""

from pathlib import Path
import camelot  ## REQ pip install opencv-python \ https://www.ghostscript.com/download/gsdnld.html
from tabulate import tabulate


# PATH TO FILE 
data_folder = Path(Path.cwd(),  "tables")
dataset_path = Path(data_folder, "food.pdf")



tables = camelot.read_pdf(str(dataset_path))
tables[0].df[1:3]


data_tech = Path(data_folder, "MGI_Disruptive_technologies_Full_report_May2013.pdf")

tables_tech = camelot.read_pdf(str(data_tech), pages="32", area=[269.875, 120.75, 790.5, 561])


# Find page with table

for i in range(30,35):
    print (i)
    tables = camelot.read_pdf(str(data_tech), pages='%d' %  i)
    try:
        print (tabulate(tables[0].df))
        print (tabulate(tables[1].df))
    except IndexError:
        print('None')