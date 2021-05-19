# views.py
from django.shortcuts import render, redirect

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseNotFound


def pdf_view(request):
    image_data = open("C:/Users/Kaan/PycharmProjects/temp/mysite/media/mypdf.pdf", "rb").read()
    return HttpResponse(image_data, content_type="application/pdf")