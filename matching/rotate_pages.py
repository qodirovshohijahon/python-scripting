#!/usr/bin/env python

from PyPDF2 import PdfFileReader, PdfFileWriter

def rotate_pages(pdf_path):
    pdf_writer = PdfFileWriter()
    pdf_reader = PdfFileReader(pdf_path)
    
    page_1 = pdf_reader.getPage(0).rotateClockwise(90)
    pdf_writer.addPage(page_1)
    page_2 = pdf_reader.getPage(1).rotateCounterClockwise(90)
    pdf_writer.addPage(page_2)
    pdf_writer.addPage(pdf_reader.getPage(2))
    
    with open('rotate_page.pdf', 'wb') as out:
        pdf_writer.write(out)
        
        
if __name__ == '__main__':
    path = '/home/mustofa/Downloads/chapter1.pdf'
    rotate_pages(path)