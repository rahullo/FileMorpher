from django.urls import path
from . import views

urlpatterns = [
    path('fileMorpher/', views.home, name='home'),
    path('fileMorpher/docTopdf', views.docTopdf, name='docTopdf'),
    path('fileMorpher/pdfTodoc', views.pdfTodoc, name='pdfTodoc'),
    path('fileMorpher/jpgtopdf', views.jpgTopdf, name='jpgTopdf'),
    path('fileMorpher/pdftojpg', views.pdfTojpg, name='pdfTojpg'),
    path('fileMorpher/watermark', views.watermark, name='watermark'),
    path('fileMorpher/bgremover', views.bgremover, name='bgremover')
]