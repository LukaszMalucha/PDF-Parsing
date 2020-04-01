# -*- coding: utf-8 -*-

import io
from pathlib import Path
import datetime
import json
import shutil
from PIL import Image
import pytesseract
import fitz
import csv

import pandas as pd



# PATH TO TESSERACT OCRT
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
#text=(pytesseract.image_to_string(Image.open("outfile.png")))
#text=repr(text)
#print(text)




def get_file_brand(string, tuples):
    """Function that retrieve brand for given pdf file"""
    for element in tuples:
        if string == element[1]:
            return element[0]
    return "NA"     
        
def get_file_product(string, tuples):
    """Function that retrieve brand for given pdf file"""
    for element in tuples:
        if string == element[1]:
            return element[2]
    return "NA"      


# Time and date
CURRENT_DATE = datetime.datetime.now().strftime("%Y-%m-%d")
TIME_NOW = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

# Folder Paths
PDFS = list(Path(Path.cwd(),  "PDFS").glob('*.pdf'))
EXTRACTED_PATH = Path(Path.cwd(),  "EXTRACTED_FILES")


# File Names + Brands Tuples
dataset_brands = pd.read_csv("pdf_brand_names.csv", encoding='utf-8-sig') 
pdf_tuples = [tuple(x) for x in dataset_brands.to_numpy()]



def extract_pdf_page(filename, input_file, brand):
    
    
    # Paths for creating folder and file
    output_file_folder = Path(EXTRACTED_PATH, brand, input_file)
    output_file_folder.mkdir(parents=True, exist_ok=True)
    
    # Copy PDF to new folder            
    shutil.copy(str(filename), str(output_file_folder))
    

    doc = fitz.open(filename)   
    page_count = len(doc) # Page Count
    pages = []        


    
    for i in range(page_count):   
        print(i)
        page = doc.loadPage(i)
        pix = page.getPixmap()
        output = (str(output_file_folder) + "//" + "page_%s.jpg" % (i))
        pix.writePNG(output)
        page=(pytesseract.image_to_string(Image.open(output)))
        page = page.replace("\n", " ")
        pages.append(page)
        Path(output).unlink()
        
        
    text_file_folder = Path(EXTRACTED_PATH, brand, input_file, "pages")    
    text_file_folder.mkdir(parents=True, exist_ok=True)
    text_file_path = Path(text_file_folder,input_file + "-page-1" + ".csv")
    with open(text_file_path, 'w', encoding="utf-8-sig") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(pages)          





def pdf_extractor():
    """Extractor compiler with report creation"""    
    # Create directory if doesn't exist already
    EXTRACTED_PATH.mkdir(parents=True, exist_ok=True)    
    
    # Report data dict
    report_dict = dict()       
    date_time = TIME_NOW
    issue_count = 0
    issues = []
    successful_count = 0
    
    
    for document in PDFS:
        input_file_name = Path(document).stem
        input_file_brand = get_file_brand(input_file_name, pdf_tuples)
        
        try:
            extract_pdf_page(document, input_file_name, input_file_brand)
            successful_count += 1
            document.unlink()
        # catch errors for further review    
        except Exception as e:            
            issue_count += 1
            message = "Failed to process {0} {1}. EXCEPTION: {2}".format(str(input_file_brand), str(input_file_name), str(e))
            issues.append(message)          
            pass   
        

                
            
   
    report_dict['report_time'] = date_time
    report_dict['issue_count'] = issue_count
    report_dict['successful_count'] = successful_count
    report_dict['issues'] = issues
    
    

    
    
    # Save data as json
    report_file_path = Path(EXTRACTED_PATH , "Report-"  + CURRENT_DATE + ".json")    
    with open(report_file_path, 'w') as fp:
        json.dump(report_dict, fp)
        
  
# Execute    
pdf_extractor()   




