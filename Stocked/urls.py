from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='Stocked'),
    path('Stores/',views.Stores,name='Stores')
]