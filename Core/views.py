from django.shortcuts import render
# Create your views here.

def Home(request):
    Context ={
        'Breadcrumbs':{'Home':'Home.html'},
      }
    return render(request,'Home.html',Context)