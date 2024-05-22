
from django.shortcuts import render 
# Create your views here.


def Stocked(request,template_name):
    Context ={'PageName':template_name,'template':'includes/'+template_name+'.html','New':'#New'+template_name+'Modal',
              'Breadcrumbs':['Stock',template_name]}
    

    return render(request,'Stocked.html',Context)
