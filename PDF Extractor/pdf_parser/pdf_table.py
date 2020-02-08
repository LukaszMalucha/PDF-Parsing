# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 08:23:30 2020

@author: LukaszMalucha
"""

import tabula as tb
from tabulate import tabulate
from pathlib import Path



# PATH TO FILE 
data_folder = Path(Path.cwd(),  "tables")
dataset_path = Path(data_folder, "food.pdf")

df_1 = tb.read_pdf(dataset_path, pages=3)[0]
df_1 = df_1.dropna(axis="rows")



df_all = tb.read_pdf(dataset_path, pages="all", multiple_tables=True)



dataset = tb.read_pdf(dataset_path, encoding = "ISO-8859-1", 
                      stream=True, area = [269.875, 12.75, 790.5, 961],
                      pages = 4,
                      guess = False,  
                      pandas_options={'header':None})
