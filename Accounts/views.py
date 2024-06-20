from typing import Any
from django.shortcuts import render,redirect
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from .models import Account 
# Create your views here.


class listView(ListView):
    template_name ='Accounts.html'
    def get_queryset(self) :
        model = Account
        account_type = self.kwargs['template_name'][:-1].lower()
        return model.objects.filter(type=account_type)
    
    def get_context_data(self):
        template_name = self.kwargs['template_name']
        object_lIst = self.get_queryset()
        Context ={'template':template_name,
              'Breadcrumbs':['Accounts',template_name],
              'object_list' : object_lIst}
        return Context
    

   
class createView(CreateView):
    fields = '__all__'
    template_name = 'create.html'
    
    def get_queryset(self) :
        model = Account
        account_type = self.kwargs['template_name'][:-1].lower()
        return model.objects.filter(type=account_type)
    
    def form_valid(self, form):
        form.save()
        template = self.kwargs['template_name']
        return redirect(f'http://127.0.0.1:8000/Accounts/{template}')

class updateView(UpdateView):
    fields = '__all__'
    template_name = 'update.html'

    def get_object(self):
        model = Account
        pk = self.kwargs['pk']
        return model.objects.get(pk=pk)
    
    def form_valid(self, form):
        form.save()
        template = self.kwargs['template_name']
        return redirect(f'http://127.0.0.1:8000/Accounts/{template}')
    
class deleteView(DeleteView):
    template_name = 'delete.html'

    def get_object(self):
        model = Account
        pk = self.kwargs['pk']
        return model.objects.get(pk=pk)
    
    def get_success_url(self) -> str:
        template = self.kwargs['template_name']
        return redirect(f'http://127.0.0.1:8000/Accounts/{template}')
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = {}
        if self.object :
            context['object'] = self.object
            context['CancelUrl'] = self.get_success_url()
        return context
    
    def delete(self,request,*args,**kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delet()
        return redirect(success_url)
        