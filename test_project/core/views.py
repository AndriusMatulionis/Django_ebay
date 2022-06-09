from django.shortcuts import render
from django.http import HttpResponse
from .models import Scrape

def all_scraped_data(request):
    scraped_list = Scrape.objects.all()
    render(request, 'core/templates/index.html',
        {'scraped_list': scraped_list })

def index(request):
    
    return render(request,'index.html')

