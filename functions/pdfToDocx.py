# FILE_PATH = r'C:\Users\hp\Desktop\DSAwithMe\DSAwithMe\PYTHON\FileConverter\pdf\epan.pdf'

from pdf2docx import Converter

def pdfConverter(pdf, pdfName):

    # pdf_file = r'C:\Users\hp\Desktop\DSAwithMe\DSAwithMe\PYTHON\FileConverter\exam3.pdf'

    word_file = f'{pdfName}.docx'

    cv = Converter(pdf)

    cv.convert(word_file, start=0, end=None)
    cv.close()


pdfConverter(r'C:\Users\hp\Desktop\DocumentConverter\pdf\pdf1.pdf', 'pdf1')