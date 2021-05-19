#urls.py
from django.contrib import admin
from django.urls import path
from pages import views
from django.conf.urls import url
urlpatterns = [
    path('', views.pdf_view, name='pdf_view')
]