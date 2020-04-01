# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 18:59:40 2020

@author: LukaszMalucha
"""

from pathlib import Path


import shutil


BRANDS = ['YORK', 'PENN Controls', 'Kantech', 'Johnson Controls', 'CEM Systems', 'Quantech', 'Exacq', 
          'CHEMGUARD', 'ANSUL', 'Luxaire', 'Fraser-Johnston', 'Coleman', 'Triatek', 'Simplex', 'Sensormatic', 
          'SKUM', 'HYGOOD', 'LPG', 'GEM', 'FIREATER', 'SABO FOAM', 'NEURUPPIN', 'THORN SECURITY', 
          'Facility Explorer', 'Autocall', 'TempMaster', 'Metasys', 'Verasys', 'BCPro', 'Champion', 'LUX', 'Tyco', 'PEAK', 'Ruskin', 'PYRO-CHEM', 'WILLIAMS']



FOLDERS = []
for brand in BRANDS:
    try:
        CURRENT_PATH = Path(Path.cwd(), brand)
        BRAND_FOLDERS = [str(x) for x in CURRENT_PATH.iterdir() if x.is_dir()]  
        for element in BRAND_FOLDERS:      
            FOLDERS.append(element)
    except:
        pass





def find_empty():
    """Compiler for html text extraction"""
    error_folder = Path(Path.cwd(), "ERROR")
    error_folder.mkdir(parents=True, exist_ok=True) 
    no_pdf = []
    for i, folder in enumerate(FOLDERS):
        try:
            pdf = list(Path(folder).glob("*.pdf"))
            if len(pdf) > 0:
                pages = list(Path(folder, "pages").glob('*.csv'))
                
                if len(pages) == 0:
                    shutil.copy(str(pdf), str(error_folder))
        except:
            no_pdf.append(str(pdf))
            
    return no_pdf        
            
            

        


find_empty()
    