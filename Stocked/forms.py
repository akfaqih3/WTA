from django.forms import ModelForm
from .models import *


class StoreForm(ModelForm):
    
    class Meta:
        model = Store
        fields = '__all__'