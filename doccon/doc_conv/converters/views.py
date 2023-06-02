from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from flask import Flask, request, redirect, url_for
app = Flask(__name__)


import pythoncom

from pdf2docx import Converter
from docx2pdf import convert
import img2pdf
from pdf2image import convert_from_path, convert_from_bytes

import pandas as pd
import string
import random
import os
from zipfile import ZipFile
import re


import docx2pdf

# Create your views here.

def home(request):
    template = loader.get_template('home.html')

    return HttpResponse(template.render())


def docTopdf(request):
    pythoncom.CoInitialize()

    if request.method == 'POST':
        print("I am in...")
        res = ''.join(random.choice(string.ascii_lowercase) for x in range(10))
        path_to_upload = os.path.join('./converters/static/uploaded_files/doc2pdf', str(res))
        os.makedirs(path_to_upload)
        files = request.FILES
        for file in files.getlist('files'):
            with open(path_to_upload + '/sample.docx', 'wb+') as f:
                for chunk in file.chunks():
                    f.write(chunk)

        convert(path_to_upload+'/sample.docx')

        return render(request, 'doctopdf.html', {'url': str(res)})
    return render(request, 'doctopdf.html')





def pdfTodoc(request):
    pythoncom.CoInitialize()

    if request.method == 'POST':
        res = ''.join(random.choice(string.ascii_lowercase) for x in range(10))
        path_to_upload = os.path.join('./converters/static/uploaded_files/pdf2doc', str(res))
        os.makedirs(path_to_upload)
        files = request.FILES
        for file in files.getlist('files'):
            with open(path_to_upload + '/sample.pdf', 'wb+') as f:
                for chunk in file.chunks():
                    f.write(chunk)

        cv = Converter(path_to_upload+'/sample.pdf')
        cv.convert(path_to_upload+'/sample.docx', start=0, end=None)
        cv.close()

        return render(request, 'pdftodoc.html', {'url': str(res)})
    return render(request, 'pdftodoc.html')


def jpgTopdf(request):
    pythoncom.CoInitialize()

    if request.method == "POST":
        res = ''.join(random.choice(string.ascii_lowercase) for x in range(10))
        path_to_upload = os.path.join('./converters/static/uploaded_files/jpg2pdf/', str(res))
        os.makedirs(path_to_upload)
        files = request.FILES
        files_list = []
        for file in files.getlist('files'):
            files_list.append(file)

        a4inpt = (img2pdf.mm_to_pt(210), img2pdf.mm_to_pt(297))
        layout_fun = img2pdf.get_layout_fun(a4inpt)
        with open(path_to_upload + "/sample.pdf", "wb") as f:
            f.write(img2pdf.convert(files_list, layout_fun=layout_fun))
        # os.rename(path_to_upload + "/sample.pdf", path_to_upload + "/sample.pdf")
        return render(request, 'jpgtopdf.html', {'url': str(res)})
    return render(request, 'jpgtopdf.html')




# def pdfTojpg(request):
#     pythoncom.CoInitialize()


#     if request.method == "POST":
#         res = ''.join(random.choice(string.ascii_lowercase) for x in range(10))
#         path_to_upload = os.path.join('./converters/static/uploaded_files/pdf2jpg', str(res))
#         os.makedirs(path_to_upload)
#         files = request.FILES
#         for file in files.getlist('files'):
#             with open(path_to_upload + '/sample.pdf', 'wb+') as f:
#                 for chunk in file.chunks():
#                     f.write(chunk)

#         images = convert_from_path(path_to_upload + '/sample.pdf', 500)

#         zipObj = ZipFile(path_to_upload + '/sample.zip', 'w')
 
#         for image in images:
#             image.save("/page%d.jpg" % (images.index(image)), "JPEG")
#             zipObj.write("/page%d.jpg" % (images.index(image)))
#             os.remove("/page%d.jpg" % (images.index(image)))

#         zipObj.close()
#         os.remove(path_to_upload + "/sample.pdf")
#         os.rename(path_to_upload + "/sample.zip", path_to_upload + "/sample.txt")
#         return render(request, 'pdftojpg.html', {'url': str(res)})
#     return render(request, 'pdftojpg.html')

def pdfTojpg(request):
    pythoncom.CoInitialize()

    if request.method == "POST":
        res = ''.join(random.choice(string.ascii_lowercase) for x in range(10))
        path_to_upload = os.path.join('./converters/static/uploaded_files/pdf2jpg', str(res))
        os.makedirs(path_to_upload)
        files = request.FILES
        files_list = []
        for file in files.getlist('files'):
            with open(path_to_upload + '/sample.pdf', 'wb+') as f:
                for chunk in file.chunks():
                    f.write(chunk)

        images = convert_from_path(path_to_upload+'/sample.pdf', 500, poppler_path = r"C:\Users\hp\Downloads\Release-23.05.0-0\poppler-23.05.0\Library\bin")
        
        for i in range(len(images)):
            
            # images[i].save(r'C:\Users\hp\Desktop\DJANGO\FileMorpher\doccon\doc_conv\converters\static\uploaded_files\pdf2jpg\{str}}\sample.jpg', 'JPEG')
            images[i].save(path_to_upload+'/sample.jpg', 'JPEG')

        os.remove(path_to_upload+'/sample.pdf')

        return render(request, 'pdftojpg.html', {'url': str(res)})
        
    return render(request, 'pdftojpg.html')

