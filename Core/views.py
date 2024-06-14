from django.shortcuts import render
from Stocked.forms import *
# Create your views here.

def Home(request):
    Context ={
        'PageName':'',
        'Breadcrumbs':{'Home':'Home.html'},
        'Forms':{
            'Store':StoreForm
        }}
    return render(request,'Home.html',Context)