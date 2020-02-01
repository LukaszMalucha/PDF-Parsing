# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 12:13:55 2020

@author: LukaszMalucha
"""

import fitz  # REQ pip install PyMuPDF

doc = fitz.open("image.pdf")
for i in range(len(doc)):
    for img in doc.getPageImageList(i):
        xref = img[0]
        pix = fitz.Pixmap(doc, xref)
        if pix.n < 5:       # this is GRAY or RGB
            pix.writePNG("p%s-%s.png" % (i, xref))
        else:               # CMYK: convert to RGB first
            pix1 = fitz.Pixmap(fitz.csRGB, pix)
            pix1.writePNG("p%s-%s.png" % (i, xref))
            pix1 = None
        pix = None            