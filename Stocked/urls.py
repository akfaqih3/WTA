from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='Stocked'),
    path('Stores/',views.Stores,name='Stores'),
    path('Brands/',views.Brands,name='Brands'),
    path('Categories/',views.Categories,name='Categories'),
    path('Units/',views.Units,name='Units'),
    path('Products/',views.Products,name='Products')
]