#!/usr/bin/env python

from PyPDF2 import PdfFileReader



def main():
    file_name = '/home/mustofa/Documents/it_books/kubernetes-for-full-stack-developers.pdf'
    pdfFile = PdfFileReader(file_name, 'rb')
    pdf_data = pdfFile.getDocumentInfo()
    print("----Metadata----")
    for md in pdf_data:
        print(md+":", pdf_data[md])
        
        
        
if __name__ == '__main__':
    main()