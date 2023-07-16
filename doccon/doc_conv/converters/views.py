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
import cv2

import pandas as pd
import string
import random
import os
from zipfile import ZipFile
import re
import numpy as np

import time
from threading import Timer


import docx2pdf

# Create your views here.


def home(request):
    template = loader.get_template('home.html')

    return HttpResponse(template.render())

def my_function(*arg1):
    os.remove(arg1[0])
    os.rmdir(arg1[0][:53])


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

        timer = Timer(25, my_function, {path_to_upload+'/sample.pdf': "hello" })
        timer.start()

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

        timer = Timer(25, my_function, {path_to_upload+'/sample.docx': "hello" })
        timer.start()

        return render(request, 'pdftodoc.html', {'url': str(res)})
    return render(request, 'pdftodoc.html')

#Convert JPG to PDF
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


        timer = Timer(25, my_function, {path_to_upload+'/sample.pdf': "hello" })
        timer.start()
        
        return render(request, 'jpgtopdf.html', {'url': str(res)})
    
    return render(request, 'jpgtopdf.html')


#Convert pdf to jpg
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

        
        timer = Timer(25, my_function, {path_to_upload+'/sample.jpg': "hello" })
        timer.start()

        return render(request, 'pdftojpg.html', {'url': str(res)})
        
    return render(request, 'pdftojpg.html')


#Remove your background from your image
def bgremover(request):
    pythoncom.CoInitialize()

    if request.method == "POST":
        res = ''.join(random.choice(string.ascii_lowercase) for x in range(10))
        path_to_upload = os.path.join('./converters/static/uploaded_files/bgremover', str(res))
        os.makedirs(path_to_upload)
        files = request.FILES
        for file in files.getlist('files'):
            with open(path_to_upload + '/sample.jpg', 'wb+') as f:
                for chunk in file.chunks():
                    f.write(chunk)

        # Alternate method
        # Read the image
        image = cv2.imread(path_to_upload + '/sample.jpg')
        # print(path_to_upload + '/sample.jpg')
        # # Convert image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # # Apply thresholding to create a binary mask
        _, binary_mask = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

        # # Perform morphological operations to improve mask
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
        morphed_mask = cv2.morphologyEx(binary_mask, cv2.MORPH_OPEN, kernel, iterations=3)

        # # Apply the mask to the original image
        result = cv2.bitwise_and(image, image, mask=morphed_mask)

        # Save the result
        cv2.imwrite(path_to_upload + '/output.jpg', result)

        # images = convert_from_path(path_to_upload+'/sample.jpg', 500, poppler_path = r"C:\Users\hp\Downloads\Release-23.05.0-0\poppler-23.05.0\Library\bin")
        
        # for i in range(len(images)):
        #     images[i].save(path_to_upload+'/sample.jpg', 'JPEG')

        # os.remove(path_to_upload+'/sample.jpg')

        
        timer = Timer(2500, my_function, {path_to_upload+'/sample.jpg': "hello" })
        timer.start()

        return render(request, 'bgremover.html', {'url': str(res)})
        
    return render(request, 'bgremover.html')



def watermark(request):
    pythoncom.CoInitialize()

    if request.method == "POST":
        res = ''.join(random.choice(string.ascii_lowercase) for x in range(10))
        path_to_upload = os.path.join('./converters/static/uploaded_files/watermark', str(res))
        os.makedirs(path_to_upload)
        files = request.FILES
        print(files.getlist('files'))
        for file in files.getlist('files'):
            print(file)
            with open(path_to_upload + '/sample.pdf', 'wb+') as f:
                for chunk in file.chunks():
                    f.write(chunk)

        # images = convert_from_path(path_to_upload+'/sample.pdf', 500, poppler_path = r"C:\Users\hp\Downloads\Release-23.05.0-0\poppler-23.05.0\Library\bin")
        
        # for i in range(len(images)):
        #     images[i].save(path_to_upload+'/sample.jpg', 'JPEG')

        # os.remove(path_to_upload+'/sample.pdf')

        
        # timer = Timer(25, my_function, {path_to_upload+'/sample.jpg': "hello" })
        # timer.start()

        return render(request, 'watermark.html', {'url': str(res)})
        
    return render(request, 'watermark.html')
