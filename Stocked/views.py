from django.shortcuts import render
from pathlib import Path
# Create your views here.

def index(request):
    Context ={ 'base':Path(__file__).resolve(),'PageName':'',
              'Breadcrumbs':{'Home':'Home.html','Stock':'Stock.html'}}
    return render(request,'index.html',Context)

def Stores(request):
    Context ={ 'base':Path(__file__).resolve(),'PageName':'Stores',
              'Breadcrumbs':{'Home':'Home.html','Stock':'Stock.html','Stores':'Stores.html'}}
    return render(request,'index.html',Context)
