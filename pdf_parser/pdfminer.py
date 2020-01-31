# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 16:39:34 2020

@author: LukaszMalucha
"""



import io
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage
def extract_text_by_page(pdf_path):
    with open(pdf_path, 'rb') as fh:
        for page in PDFPage.get_pages(fh, 
                                      caching=True,
                                      check_extractable=True):
            resource_manager = PDFResourceManager()
            fake_file_handle = io.StringIO()
            converter = TextConverter(resource_manager, fake_file_handle)
            page_interpreter = PDFPageInterpreter(resource_manager, converter)
            page_interpreter.process_page(page)
            
            text = fake_file_handle.getvalue()
            yield text
    
            # close open handles
            converter.close()
            fake_file_handle.close()
            

def extract_text(pdf_path):
    for page in extract_text_by_page(pdf_path):
        print(page)
        print()
            
    
pdf_data = extract_text('food.pdf')


## DO SKRYPTU


cd c:\Anaconda3\Scripts
python pdf2txt.py -o e:\food.html c:\food.pdf
python pdf2txt.py -o e:\food.xml c:\food.pdf

