from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static
app_name = 'Stocked'

urlpatterns=[
    path('<template_name>/',views.listView.as_view(),name='Stocked'),
    path('create/<template_name>/',views.createView.as_view(),name='create'),
    path('update/<str:template_name>/<int:pk>/',views.updateView.as_view(),name='update'),
    path('delete/<str:template_name>/<int:pk>/',views.deleteView.as_view(),name='delete'),
]
urlpatterns += static(settings.MEDIA_URL,
                          document_root = settings.MEDIA_ROOT)