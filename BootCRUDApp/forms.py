from django import forms
from .models import sellItem

# this is the for that is used to add items

class sellItemform(forms.ModelForm):
    class Meta():
        fields = '__all__'
        model = sellItem