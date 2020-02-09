# -*- coding: utf-8 -*-


from pathlib import Path
import camelot  ## REQ pip install opencv-python \ https://www.ghostscript.com/download/gsdnld.html



from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument

from pdfminer.pdfinterp import resolve1

file_path = Path(Path.cwd(), "image.pdf")

file = open(str(file_path), 'rb')
parser = PDFParser(file)
document = PDFDocument(parser)

        
        

tables_list = []


    
tables = camelot.read_pdf(str(file_path), pages="all")


for i in range(0,1):
    print (i)
    tables = camelot.read_pdf("image.pdf", pages='%d' %  i)
    try:
        print (tabulate(tables[0].df))
        print (tabulate(tables[1].df))
    except IndexError:
        print('None')
        
        

tables.export('image.csv', f='csv', compress=False)    
tables[0].parsing_report    

for element in tables:
    lists = element.df.values.tolist()
    tables_list.append(element.df.to_dict())
    tables_list.append(lists)

dictus = tables[1].df.to_dict()


