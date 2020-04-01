# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 18:59:40 2020

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





FOLDERS = []
for brand in BRANDS:
    try:
        CURRENT_PATH = Path(Path.cwd(), brand)
        BRAND_FOLDERS = [str(x) for x in CURRENT_PATH.iterdir() if x.is_dir()]  
        for element in BRAND_FOLDERS:      
            FOLDERS.append(element)
    except:
        pass





def count_characters():

    error_folder = Path(Path.cwd(), "ERROR")
    error_folder.mkdir(parents=True, exist_ok=True) 
    no_pdf = []
    
    for i, folder in enumerate(FOLDERS):
        print(i)
        pdf = list(Path(folder).glob("*.pdf"))
        total_folder = Path(folder, "Character Count")
        total_folder.mkdir(parents=True, exist_ok=True) 
        total_file_path = Path(total_folder, "page_count.csv")
        character_count_path = Path(folder, "character_count.csv")
        
        
        try:
            pages = list(Path(folder, "pages").glob("*.csv"))       
            
            if len(pages) > 0:      
                dataset = pd.DataFrame(columns=dataframe_columns)                                        
                for page in pages:
                    d_dict = defaultdict(int)
                    with open(page, encoding="utf-8") as f:   
                        s = f.read()
                        for char in s:
                            char = char.lower()
                            if char in character_set:
                                d_dict[char] += 1               
                   
                    d_dict  = dict(sorted(d_dict.items(), key=lambda v:v[1], reverse=True))
                    
                    dataset = dataset.append(d_dict, ignore_index=True)   
                dataset.loc["Total", :] = dataset.sum(axis=0)  
                
                total_dataset = dataset[-1:]
                dataset.to_csv(total_file_path, encoding='utf-8', index=False)  
                total_dataset.to_csv(character_count_path, encoding='utf-8', index=False)
                
            else:
               shutil.copy(str(pdf), str(error_folder))         
        except:
            no_pdf.append(str(pdf))
            
    return dataset     
            
            

        


lst = count_characters()





















