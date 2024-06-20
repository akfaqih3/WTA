from django.urls import path
from . import views

app_name = 'Accounts'
urlpatterns=[
    path('<template_name>/',views.listView.as_view(),name='accounts'),
    path('create/<template_name>/',views.createView.as_view(),name='create'),
    path('update/<str:template_name>/<int:pk>/',views.updateView.as_view(),name='update'),
    path('delete/<str:template_name>/<int:pk>/',views.deleteView.as_view(),name='delete'),
]