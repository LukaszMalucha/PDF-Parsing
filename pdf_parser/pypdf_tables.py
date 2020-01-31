# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 10:59:17 2020

@author: LukaszMalucha
"""

from pathlib import Path
import PyPDF2 as p2
import numpy


# PATH TO FILE 
data_folder = Path(Path.cwd(),  "tables")
dataset_path = Path(data_folder, "food.pdf")

read_pdf = p2.PdfFileReader(open(dataset_path, 'rb'))
number_of_pages = read_pdf.getNumPages()
page = read_pdf.getPage(2)
page_content = page.extractText()
print(page_content.encode('utf-8'))


## REBUILD TABLE
page_content = page_content.replace('300 cal\ns Medium', '300 cals\n Medium')
page_content = page_content.replace('300 cal\ns Medium', '300 cals\n Medium')
page_content = page_content.replace('Liver\n pate', 'Liver pate')
page_content = page_content.replace('\n ', ';')
#print(page_content.encode('utf-8'))
page_content = page_content.replace('\n-', '-')
#print(page_content.encode('utf-8'))
page_content = page_content.replace('\n', '')
#print(page_content.encode('utf-8'))
page_content = page_content.replace('Ham 6 cals', 'Ham; 6 cals')
#print(page_content.encode('utf-8'))
table_list = page_content.split(';')
table_list = list(filter(None, table_list))


print(len(table_list))
row = numpy.array_split(table_list, 30)
for i in range(0,30):
    print(row[i])