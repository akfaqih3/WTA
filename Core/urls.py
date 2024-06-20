from django.urls import path,include
from . import views

urlpatterns=[
    path('',views.Home,name='Home'),
    path('Stocked/',include('Stocked.urls'),name='Stocked'),
    path('Accounts/',include('Accounts.urls'),name='Accounts')
]