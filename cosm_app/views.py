from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from cosm_app.forms import AddProductType, AddActivity
from cosm_app.models import Producer, ProductType, Product,Activity


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
        producers = Producer.objects.all()
        return render(request,'add_producer.html',{'product_types': product_types, 'producers':producers})

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

class AddProductView(View):
    def get(self,request):
        product_types = ProductType.objects.all()
        producers = Producer.objects.all()
        return render(request, 'add_product.html', {'product_types': product_types,'producer':producers})

    def post(self,request):
        name = request.POST.get('name')
        price = request.POST.get('price')
        product_type_id = request.POST.get('producttype_id')
        product_type = ProductType.objects.get(id=product_type_id)
        producer_id = request.POST.get('producer_id')
        producer = Producer.objects.get(id=producer_id)
        Product.objects.create(name=name, price=price, product_type=product_type, producer=producer)
        return redirect('add_product')


class ProductView(View):
    def get(self,request):
        products = Product.objects.all()
        return render(request,'products.html', {'products' : products})

class AddActivityView(View):
    def get(self,request):
        form = AddActivity()
        return render(request, 'add_activity.html', {'form': form})

    def post(self,request):
        form = AddActivity(request.POST)
        if form.is_valid():
            name = request.POST.get('name')
            price = request.POST.get('price')
            time = request.POST.get('time')
            description = request.POST.get('description')
            Activity.objects.create(name=name, price=price, time=time, description=description)
        return redirect('activities')

class ActivityView(View):
    def get(self,request):
        activities = Activity.objects.all()
        return render(request,'activities.html', {'activities': activities})