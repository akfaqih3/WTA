from django.shortcuts import render
from pathlib import Path
# Create your views here.

def index(request):
    Context ={'PageName':'','Page':'includes/index.html',
              'Breadcrumbs':{'Home':'Home.html','Stock':'Stock.html'}}
              
    return render(request,'index.html',Context)

def Stores(request):
    Context ={'PageName':'Stores','Page':'includes/Stores.html',
              'Breadcrumbs':{'Home':'Home.html','Stock':'Stock.html','Stores':'Stores.html'}}
              
    return render(request,'index.html',Context)

def Categories(request):
    Context ={'PageName':'Categories','Page':'includes/Categories.html',
              'Breadcrumbs':{'Home':'Home.html','Stock':'Stock.html','Categories':'Categories.html'}}
              
    return render(request,'Categories.html',Context)

def Units(request):
    Context ={'PageName':'Units','Page':'includes/Units.html',
              'Breadcrumbs':{'Home':'Home.html','Stock':'Stock.html','Units':'Units.html'}}
              
    return render(request,'Units.html',Context)

def Products(request):
    Context ={'PageName':'Products','Page':'includes/Products.html',
              'Breadcrumbs':{'Home':'Home.html','Stock':'Stock.html','Products':'Products.html'}}
    
    return render(request,'Products.html',Context)
