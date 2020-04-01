# -*- coding: utf-8 -*-

import shutil
from pathlib import Path
import pandas as pd




BRANDS = ['YORK', 'PENN Controls', 'Kantech', 'Johnson Controls', 'CEM Systems', 'Quantech', 'Exacq', 
          'CHEMGUARD', 'ANSUL', 'Luxaire', 'Fraser-Johnston', 'Coleman', 'Triatek', 'Simplex', 'Sensormatic', 
          'SKUM', 'HYGOOD', 'LPG', 'GEM', 'FIREATER', 'SABO FOAM', 'NEURUPPIN', 'THORN SECURITY', 
          'Facility Explorer', 'Autocall', 'TempMaster', 'Metasys', 'Verasys', 'BCPro', 'Champion', 'LUX', 'Tyco', 'PEAK', 'Ruskin', 'PYRO-CHEM', 'WILLIAMS']

# Folder Paths
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
    errors_folder = Path(Path.cwd(), "EMPTY")
    errors_folder.mkdir(parents=True, exist_ok=True)   
    missing_pdf = []
    
    for i, folder in enumerate(FOLDERS):
        pages = list(Path(folder, "pages").glob('*.csv'))
        try:
            pdf = list(Path(folder).glob('*.pdf'))[0]       
            if len(pages) == 0:
                print(str(pdf))
                shutil.copy(str(pdf), str(errors_folder))
        except:
            missing_pdf.append(str(folder))
            
    df = pd.DataFrame({"Missing PDFS" : missing_pdf})
    df.to_csv("missing_pdfs.csv", encoding='utf-8-sig', index=False)
            
            
            
        

find_empty()


