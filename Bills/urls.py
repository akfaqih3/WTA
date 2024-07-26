from django.urls import path
from .views import Bill

urlpatterns=[
    path('',Bill.as_view(),name='Bill'),
]