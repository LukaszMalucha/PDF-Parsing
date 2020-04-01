# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 14:27:24 2020

@author: LukaszMalucha
"""

from pathlib import Path
from collections import defaultdict
import pandas as pd
import shutil


BRANDS = ["YORK", "PENN Controls", "Kantech", "Johnson Controls", "CEM Systems", "Quantech", "Exacq", 
          "CHEMGUARD", "ANSUL", "Luxaire", "Fraser-Johnston", "Coleman", "Triatek", "Simplex", "Sensormatic", 
          "SKUM", "HYGOOD", "LPG", "GEM", "FIREATER", "SABO FOAM", "NEURUPPIN", "THORN SECURITY", 
          "Facility Explorer", "Autocall", "TempMaster", "Metasys", "Verasys", "BCPro", "Champion", "LUX", "Tyco", "PEAK", "Ruskin", "PYRO-CHEM", "WILLIAMS"]


dataframe_columns = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
character_set = {"0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"}

#dataset_pdfs = pd.read_csv("pdfs.csv", encoding="utf-8")  



FOLDERS = []
for brand in BRANDS:
    try:
        CURRENT_PATH = Path(Path.cwd(), brand)
        BRAND_FOLDERS = [str(x) for x in CURRENT_PATH.iterdir() if x.is_dir()]  
        for element in BRAND_FOLDERS:      
            FOLDERS.append(element)
    except:
        pass
    


def counter_dataset():
    
    dataset_document = pd.DataFrame(columns=["title", "counter_dict"])     
    no_pdf = pd.DataFrame(columns=["folder"])
    
    for i, folder in enumerate(FOLDERS):
        print(i)
        try:
            pdf = list(Path(folder).glob("*.pdf"))[0]
            pdf_title = Path(pdf).stem
            pdf_title = pdf_title + ".pdf"
    
            dataset_counter = pd.read_csv(str(Path(folder, "character_count.csv")), encoding="utf-8")
            if dataset_counter is not None:
                dataset_counter = dataset_counter.astype(int, errors="ignore")
                counter_dict = dataset_counter.to_dict('index')
                dataset_document = dataset_document.append(pd.Series([pdf_title, str(counter_dict[0])],index = ["title", "counter_dict"]),ignore_index = True)
            else:        
                dataset_document.append(["asdasd", "NO COUNTER"])
        except:
             no_pdf = no_pdf.append(pd.Series([folder],index = ["folder"]),ignore_index = True)
            
    dataset_document.to_csv("counter_dataset.csv", encoding='utf-8', index=False)  
 
    return dataset_document   


zz = counter_dataset()
    












