# -*- coding: utf-8 -*-

import io
from pathlib import Path
import datetime
import json

from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.converter import HTMLConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import resolve1

# Images
import fitz  # REQ pip install PyMuPDF

# Tables
import camelot  ## REQ pip install opencv-python \ https://www.ghostscript.com/download/gsdnld.html




# Time and date
CURRENT_DATE = datetime.datetime.now().strftime("%Y-%m-%d")
TIME_NOW = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

# Folder Paths
PDFS = list(Path(Path.cwd(),  "long").glob('*.pdf'))
HTML_PATH = Path(Path.cwd(),  "htmls")

def extract_pdf_page(filename):
    input_file_name = Path(filename).stem
    # Paths for creating folder and file
    output_file_folder = Path(HTML_PATH, input_file_name)
    output_file_folder.mkdir(parents=True, exist_ok=True)
    output_file_path = Path(output_file_folder, input_file_name + ".html") 

    
    output_file = io.StringIO()
    laparams = LAParams()
    rsrcmgr = PDFResourceManager()
    device = HTMLConverter(rsrcmgr, output_file, laparams=laparams)
                   
            
# EXTRACTING TEXT TO HTML 
    with open(filename, 'rb') as fh:
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.get_pages(fh, caching=True, check_extractable=True):
            interpreter.process_page(page)
 
    device.close()
 
    html = output_file.getvalue()
    with open (output_file_path, 'w', encoding="utf-8" ) as fd:
        fd.write(html)
        
    output_file.close()
 
    return html

def extract_pdf_images(filename):
    """Extract Images from PDF"""    
    input_file_name = Path(filename).stem
    output_images_path = Path(HTML_PATH, input_file_name, "images")
    output_images_path.mkdir(parents=True, exist_ok=True)  
    doc = fitz.open(filename)    
    page_count = len(doc) # Page Count
    
        
    for i in range(page_count):        
        for img in doc.getPageImageList(i):                
            xref = img[0]
            pix = fitz.Pixmap(doc, xref)
            if pix.n < 5:       # GREY or RGB
                pix.writePNG(str(output_images_path) + "//" + "%s-%s-%s.png" % (input_file_name, i, xref))
            else:               # CMYK: convert to RGB first
                pix1 = fitz.Pixmap(fitz.csRGB, pix)
                pix1.writePNG(str(output_images_path) + "//" +  "%s-%s.png" % (input_file_name, i, xref))
                pix1 = None
            pix = None   
    


def extract_pdf_tables(filename):
    """Extract Tables from PDF"""
    input_file_name = Path(filename).stem
    output_tables_path = Path(HTML_PATH, input_file_name, "tables")
    output_tables_path.mkdir(parents=True, exist_ok=True)  
    
    tables = camelot.read_pdf(str(filename), pages="all")     
    tables.export(str(output_tables_path) +  "/" + str(input_file_name) + ".csv", f='csv', compress=False)     
    tables_list = []

    for element in tables:
        lists = element.df.values.tolist()
        tables_list.append(element.df.to_dict())
        tables_list.append(lists) 
    




def pdf_extractor():
    """Extractor compiler with report creation"""    
    # Create directory if doesn't exist already
    HTML_PATH.mkdir(parents=True, exist_ok=True)    
    
    # Report data dict
    report_dict = dict()       
    date_time = TIME_NOW
    issue_count = 0
    issues = []
    successful_count = 0
    
    
    for document in PDFS:
        try:
            extract_pdf_page(document)
            extract_pdf_images(document)
            extract_pdf_tables(document)
            successful_count += 1
        # catch errors for further review    
        except Exception as e:            
            issue_count += 1
            message = "Failed to process {0}: {1}".format(str(document), str(e))
            issues.append(message)          
            pass   
            
            
   
    report_dict['report_time'] = date_time
    report_dict['issue_count'] = issue_count
    report_dict['successful_count'] = successful_count
    report_dict['issues'] = issues
    
    # Save data as json
    report_file_path = Path(HTML_PATH , "Report-"  + CURRENT_DATE + ".json")    
    with open(report_file_path, 'w') as fp:
        json.dump(report_dict, fp)
        
  
# Execute    
pdf_extractor()   

























