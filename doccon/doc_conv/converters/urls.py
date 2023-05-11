from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('home/docTopdf', views.docTopdf, name='docTopdf'),
    path('home/pdfTodoc', views.pdfTodoc, name='pdfTodoc'),
    path('home/jpgtopdf', views.jpgTopdf, name='jpgTopdf'),
    path('home/pdftojpg', views.pdfTojpg, name='pdfTojpg'),
]