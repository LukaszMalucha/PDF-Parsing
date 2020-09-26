# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 15:49:30 2020

@author: LukaszMalucha
"""

import PyPDF2


myfile = open("test.pdf", mode="rb")


pdf_reader = PyPDF2.PdfFileReader(myfile)

pdf_reader.numPages

page_one = pdf_reader.getPage(0)

mytext = page_one.extractText()

mytext.close()





