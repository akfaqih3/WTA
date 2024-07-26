from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

class Bill(TemplateView):
    template_name = 'bill.html'
