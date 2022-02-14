from django import forms
from django.core.exceptions import ValidationError



class AddProducerForm(forms.Form):
    name = forms.CharField()

class AddProductType(forms.Form):
    product_type = forms.CharField()
    product_type_plural = forms.CharField()