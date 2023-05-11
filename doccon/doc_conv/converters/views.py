from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from flask import Flask, request, redirect, url_for
app = Flask(__name__)

from docx2pdf import convert

import pythoncom

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
        res = ''.join(random.choice(string.ascii_lowercase) for x in range(10))
        path_to_upload = os.path.join('./converters/static/uploaded_files/doc2pdf', str(res))
        os.makedirs(path_to_upload)
        files = request.FILES
        for file in files.getlist('files'):
            with open(path_to_upload + '/sample.docx', 'wb+') as f:
                for chunk in file.chunks():
                    f.write(chunk)

        convert(path_to_upload+'/sample.docx')
        
        # if file:
        #     with open(path_to_upload + "/sample.pdf", "wb") as f:
        #         print("🎇🎇🎇")
        #         f.write(docx2pdf.convert(file))
        
        # os.rename(path_to_upload + "/sample.pdf")
        # return render(request, 'doctopdf.html')

        return render(request, 'doctopdf.html', {'url': str(res)})
        # return HttpResponse(template.render())
    return render(request, 'doctopdf.html')
    # return HttpResponse(template.render())





def pdfTodoc(request):
    pythoncom.CoInitialize()


    template = loader.get_template('pdftodoc.html')

    return HttpResponse(template.render())

def jpgTopdf(request):
    pythoncom.CoInitialize()

    if request.method == "POST":
        # creating random folder name for each user
        res = ''.join(random.choice(string.ascii_lowercase) for x in range(10))
        path_to_upload = os.path.join('./converters/static/uploaded_files/jpg2pdf/', str(res))
        print("🙋‍♂️🙋‍♂️🙋‍♂️🙋‍♂️", path_to_upload)
        os.makedirs(path_to_upload)
        files = request.FILES
        print(request.FILES)
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




def pdfTojpg(request):
    pythoncom.CoInitialize()


    if request.method == "POST":
        # creating random folder name for each user
        res = ''.join(random.choice(string.ascii_lowercase) for x in range(10))
        path_to_upload = os.path.join('./converters/static/uploaded_files/pdf2jpg', str(res))
        os.makedirs(path_to_upload)
        files = request.FILES
        for file in files.getlist('files'):
            with open(path_to_upload + '/sample.pdf', 'wb+') as f:
                for chunk in file.chunks():
                    f.write(chunk)

        images = convert_from_path(path_to_upload + '/sample.pdf', 500)

        zipObj = ZipFile(path_to_upload + '/sample.zip', 'w')
 
        for image in images:
            image.save("/page%d.jpg" % (images.index(image)), "JPEG")
            zipObj.write("/page%d.jpg" % (images.index(image)))
            os.remove("/page%d.jpg" % (images.index(image)))

        zipObj.close()
        os.remove(path_to_upload + "/sample.pdf")
        os.rename(path_to_upload + "/sample.zip", path_to_upload + "/sample.txt")
        return render(request, 'pdftojpg.html', {'url': str(res)})
    return render(request, 'pdftojpg.html')

