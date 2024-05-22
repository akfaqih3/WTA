from django.urls import path
from . import views

urlpatterns=[
    path('<template_name>/',views.Stocked,name='Stocked')
]