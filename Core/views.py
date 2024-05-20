from django.shortcuts import render

# Create your views here.

def Home(request):
    Context ={'PageName':'','Breadcrumbs':{'Home':'Home.html'}}
    return render(request,'Home.html',Context)