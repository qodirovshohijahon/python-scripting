#!/bin/usr/env python

from PyPDF2 import PdfFileReader, PdfFileWriter

def split(path, name_of_split):
    pdf = PdfFileReader(path)
    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))
        # pdf_writer.ap
        out = f'{name_of_split}_{page}.pdf'
        with open(out, 'wb') as out_pdf:
            pdf_writer.write(out_pdf)
            
            
if __name__ == '__main__':
    path = '/home/mustofa/Downloads/chapter1.pdf'
    name_of_split = 'split'
    split(path, name_of_split)