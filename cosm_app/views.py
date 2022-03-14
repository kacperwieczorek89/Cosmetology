from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from cosm_app.forms import AddProducerForm, AddProductType
from cosm_app.models import Producer, ProductType, ProductType


class Index(View):
    def get(self, request):
        return render(request, 'base.html')

class ProducerView(View):
    def get(self, request):
        producers = Producer.objects.all()
        return render(request, 'producers.html', {'producers': producers})

class AddProducerView(View):
    def get(self,request):
        product_types = ProductType.objects.all()
        return render(request,'add_producer.html',{'product_types': product_types})

    def post(self,request):
        name = request.POST.get('name')
        product_type_id=request.POST.get('producttype_id')
        product_type = ProductType.objects.get(id=product_type_id)
        Producer.objects.create(name=name, product_types=product_type)
        return redirect('add_producer')

class AddProductTypeView(View):
    def get(self,request):
        form = AddProductType()
        return render(request, 'add_product_type.html', {'form': form})

    def post(self,request):
        form = AddProductType(request.POST)
        if form.is_valid():
            product_type = form.cleaned_data['product_type']
            product_type_plural = form.cleaned_data['product_type_plural']
            ProductType.objects.create(product_type=product_type, product_type_plural=product_type_plural)

        return render(request, 'add_product_type.html', {'form': form})