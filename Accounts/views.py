from django.shortcuts import render

# Create your views here.

def Accounts(request,template_name):
    Context ={'PageName':template_name,'template':'includes/'+template_name+'.html','New':'#New'+template_name+'Modal',
              'Breadcrumbs':['Acconts',template_name]}
    

    return render(request,'Accounts.html',Context)
