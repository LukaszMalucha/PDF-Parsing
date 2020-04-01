# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 11:12:18 2020

@author: LukaszMalucha
"""

from pathlib import Path
from scripts.html_to_text import extract_text

# Folder Paths
CURRENT_PATH = Path(Path.cwd(), "HTMLS")
FOLDERS = [str(x) for x in CURRENT_PATH.iterdir() if x.is_dir()]  






def html_compiler():
    """Compiler for html text extraction"""
    for folder in FOLDERS:
        csv_pages = list(Path(folder).glob('*.csv'))
        tables = list(Path(folder, "tables").glob('*.csv'))
        
        for element in csv_pages:
            print(element)            
            

        


html_compiler()



