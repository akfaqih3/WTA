
from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import redirect
from django.views.generic import UpdateView,DeleteView,CreateView,ListView
# Create your views here.
from .utility import *

class listView(ListView):
    template_name ='Stocked.html'
    def get_queryset(self) :
        model = get_list_by_template_name(self.kwargs['template_name'])
        return model.objects.all()
    
    def get_context_data(self):
        template_name = self.kwargs['template_name']
        object_lIst = self.get_queryset()
        Context ={'template':template_name,
              'Breadcrumbs':['Stock',template_name],
              'object_list' : object_lIst}
        return Context
    
class createView(CreateView):
    fields = '__all__'
    template_name = 'control/create.html'
    
    def get_queryset(self) -> QuerySet[Any]:
        model = get_list_by_template_name(self.kwargs['template_name'])
        return model.objects.all()
    
    def form_valid(self, form):
        form.save()
        template = self.kwargs['template_name']
        return redirect(f'http://127.0.0.1:8000/Stocked/{template}')

class updateView(UpdateView):
    fields = '__all__'
    template_name = 'control/update.html'

    def get_object(self):
        model = get_list_by_template_name(self.kwargs['template_name'])
        pk = self.kwargs['pk']
        return model.objects.get(pk=pk)
    
    def form_valid(self, form):
        form.save()
        template = self.kwargs['template_name']
        return redirect(f'http://127.0.0.1:8000/Stocked/{template}')
    
class deleteView(DeleteView):
    template_name = 'control/delete.html'

    def get_object(self):
        model = get_list_by_template_name(self.kwargs['template_name'])
        pk = self.kwargs['pk']
        return model.objects.get(pk=pk)
    
    def get_success_url(self) -> str:
        template = self.kwargs['template_name']
        return f'http://127.0.0.1:8000/Stocked/{template}'
    
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
        