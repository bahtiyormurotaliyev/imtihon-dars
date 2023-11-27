from django.shortcuts import render
from .models import catalog

def content_list(request):
       catalog = catalog.objects.all()
       return render(request, 'report.html', {'catalog': catalog})
   
