from django.urls import path,include
from . import views

urlpatterns=[
    path('',views.Home),
    path('Stocked/',include('Stocked.urls'),name='Stocked')
]