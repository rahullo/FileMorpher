from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from flask import Flask, request, redirect, url_for
app = Flask(__name__)

from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.core.files.storage import FileSystemStorage


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

import time
from threading import Timer


import docx2pdf

# Create your views here.

path = '123'

def home(request):
    template = loader.get_template('home.html')

    return HttpResponse(template.render())

def my_function(*arg1):
    print("The timer has fired!")
    print(type(arg1[0]))
    os.remove(arg1[0]+'/sample.jpg')


@require_POST
def delete_folder(request):
    # Get the name of the folder to delete.
    folder_name = request.POST['folder_name']
    print("💥💥💥💥",folder_name)
    # Delete the folder.
    storage = FileSystemStorage()
    storage.delete(folder_name)

    # Redirect to the home page.
    return redirect('home')

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

        os.remove(path_to_upload+'/sample.docx')

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

        os.remove(path_to_upload+'/sample.pdf')


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

        os.remove(path_to_upload+'/sample.jpg')
        
        return render(request, 'jpgtopdf.html', {'url': str(res)})
    
    return render(request, 'jpgtopdf.html')



def pdfTojpg(request):
    pythoncom.CoInitialize()

    if request.method == "POST":
        res = ''.join(random.choice(string.ascii_lowercase) for x in range(10))
        path_to_upload = os.path.join('./converters/static/uploaded_files/pdf2jpg', str(res))
        os.makedirs(path_to_upload)
        files = request.FILES
        for file in files.getlist('files'):
            with open(path_to_upload + '/sample.pdf', 'wb+') as f:
                for chunk in file.chunks():
                    f.write(chunk)

        images = convert_from_path(path_to_upload+'/sample.pdf', 500, poppler_path = r"C:\Users\hp\Downloads\Release-23.05.0-0\poppler-23.05.0\Library\bin")
        
        for i in range(len(images)):
            images[i].save(path_to_upload+'/sample.jpg', 'JPEG')

        os.remove(path_to_upload+'/sample.pdf')

        
        timer = Timer(10, my_function, {path_to_upload: "hello" })
        timer.start()
        return render(request, 'pdftojpg.html', {'url': str(res)})
        
    return render(request, 'pdftojpg.html')

