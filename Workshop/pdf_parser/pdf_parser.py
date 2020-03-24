# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 06:24:24 2020

@author: LukaszMalucha
"""

import os
import PyPDF2 as p2
import glob
from natsort import natsorted


# merge pdfs

#folder_path = os.path.abspath(os.path.dirname('__file__'))
#dataset_path = os.path.join(folder_path, "..\pdfs")

pdfs = glob.glob( 'C:/Users/Lukasz Malucha/Desktop/pdf_parser/pdfs/*.pdf')
new_merged_pdf = 'C:/Users/Lukasz Malucha/Desktop/pdf_parser/pdfs/new_merged_pdf.pdf'


merge_pdfs = p2.PdfFileMerger()

for pdf in natsorted(pdfs):
    merge_pdfs.append(open(pdf, 'rb'))
    

merge_pdfs.write(open(new_merged_pdf, "wb"))    



# Extract text

read_pdf = p2.PdfFileReader((open('C:/Users/Lukasz Malucha/Desktop/pdf_parser/pdfs/new_merged_pdf.pdf', 'rb')))

pdf_get_page = read_pdf.getPage(1)
#text = pdf_get_page.extractText()
pdf_get_page.extractText()