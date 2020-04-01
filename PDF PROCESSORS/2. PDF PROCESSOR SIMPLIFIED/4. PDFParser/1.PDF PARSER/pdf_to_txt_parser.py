# -*- coding: utf-8 -*-

import io
from pathlib import Path
import datetime
import json
import shutil


from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
import pandas as pd
import PyPDF2 as p2
import csv

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
    pdf_folder = Path(EXTRACTED_PATH, brand, input_file)
    pdf_folder.mkdir(parents=True, exist_ok=True) 
    error_folder = Path(EXTRACTED_PATH, "ERRORS")
    error_folder.mkdir(parents=True, exist_ok=True)     
    output_file_folder = Path(EXTRACTED_PATH, brand, input_file, "pages")
    output_file_folder.mkdir(parents=True, exist_ok=True) 
    
    # Copy PDF to new folder            
    shutil.copy(str(filename), str(pdf_folder))
    
    read_pdf = p2.PdfFileReader((open(str(filename), 'rb')))
    page_count = read_pdf.getNumPages()
    
    for i in range(page_count):
        print(i)
        page= []
        pdf_get_page = read_pdf.getPage(i)
        text = pdf_get_page.extractText()       
        if len(text) < 10:
            shutil.copy(str(filename), str(error_folder))
            
        else:    
            page.append(text)
            
            text_file_path = Path(output_file_folder, "-page-" + str(i+1) + ".csv")  
            with open(text_file_path, 'w', encoding="utf-8-sig") as csv_file:
                writer = csv.writer(csv_file, delimiter=',')
                writer.writerow(page)
                
            
    read_pdf.close()    
    






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
        input_file_name = Path(document).stem[:25]
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




