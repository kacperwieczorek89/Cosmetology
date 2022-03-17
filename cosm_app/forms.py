from django import forms
from django.core.exceptions import ValidationError


class AddProductType(forms.Form):
    product_type = forms.CharField()
    product_type_plural = forms.CharField()

class AddActivity(forms.Form):
    name = forms.CharField()
    price = forms.DecimalField()
    time = forms.IntegerField()
    description = forms.CharField(widget=forms.Textarea)