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

import fitz  # REQ pip install PyMuPDF




# Time and date
CURRENT_DATE = datetime.datetime.now().strftime("%Y-%m-%d")
TIME_NOW = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

# Folder Paths
PDFS = list(Path(Path.cwd(),  "long").glob('*.pdf'))
HTML_PATH = Path(Path.cwd(),  "htmls-" + CURRENT_DATE)

def extract_pdf_page(filename):
 
    # Paths for creating folder and file
    input_file_name = Path(filename).stem
    output_file_folder = Path(HTML_PATH, input_file_name)
    output_file_folder.mkdir(parents=True, exist_ok=True)
    output_file_path = Path(output_file_folder, input_file_name + "-" + TIME_NOW + ".html") 
    output_images_path = Path(HTML_PATH, input_file_name, "images")
    output_images_path.mkdir(parents=True, exist_ok=True)  
    
    output_file = io.StringIO()
    laparams = LAParams()
    rsrcmgr = PDFResourceManager()
    device = HTMLConverter(rsrcmgr, output_file, laparams=laparams)
    
    doc = fitz.open(filename)
    
    for i in range(len(doc)):        
        for img in doc.getPageImageList(i):                
            xref = img[0]
            pix = fitz.Pixmap(doc, xref)
            if pix.n < 5:       # this is GRAY or RGB
                pix.writePNG(str(output_images_path) + "//" + "%s-%s-%s.png" % (input_file_name, i, xref))
            else:               # CMYK: convert to RGB first
                pix1 = fitz.Pixmap(fitz.csRGB, pix)
                pix1.writePNG(str(output_images_path) + "//" +  "%s-%s.png" % (input_file_name, i, xref))
                pix1 = None
            pix = None           
        
 
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




def pdf_extractor():
    
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

























