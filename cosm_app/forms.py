from django import forms
from django.forms import ModelChoiceField

from cosm_app.models import Product,Activity,Treatment
from django.core.exceptions import ValidationError


class AddProductType(forms.Form):
    product_type = forms.CharField()
    product_type_plural = forms.CharField()

class AddActivity(forms.Form):
    name = forms.CharField()
    price = forms.DecimalField()
    time = forms.IntegerField()
    description = forms.CharField(widget=forms.Textarea)

# class AddTreatmentForm(forms.ModelForm):
#     class Meta:
#         model = Product
#
#         def __init__(self,*args,**kwargs):
#             super(AddTreatmentForm).__init__(*args,**kwargs)
#             self.fields['product'] = ModelChoiceField(queryset=Product.objects.all(), empty_label='Produkt')