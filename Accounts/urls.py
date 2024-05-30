from django.urls import path
from . import views

urlpatterns=[
    path('',views.Accounts,name='Accounts')
]