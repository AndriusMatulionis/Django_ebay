from django.shortcuts import render
from django.http import HttpResponse
from .models import Scrape
from django.views.generic import ListView
# pasiskaityt apie generic

class ScrapedListView(ListView):
    model = Scrape
    template_name = 'index.html'
    success_url = '/'
    
    
def index(request):
    
    return render(request,'index.html',)

