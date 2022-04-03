from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from django.views.generic import DetailView

from cosm_app.forms import AddProductType, AddActivity
from cosm_app.models import Producer, ProductType, Product,Activity,Treatment
from django.contrib.auth.mixins import LoginRequiredMixin

class Index(LoginRequiredMixin,View):
    def get(self, request):
        return render(request, 'base.html')

class ProducerView(View):
    def get(self, request):
        producers = Producer.objects.all()
        return render(request, 'producers_view.html', {'producers': producers})

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
        return render(request, 'activities_view.html', {'activities': activities})

class AddTreatmentView(View):
    def get(self,request):
        products = Product.objects.all()
        activities = Activity.objects.all()
        return render(request,'add_treatment.html',{'activities':activities,'products':products})

    def post(self,request):
        name = request.POST.get('name')
        products = request.POST.getlist('product_id')
        products_price = Product.objects.filter(id__in=products)
        suma_p = 0
        for p in products_price:
            suma_p += p.price

        activitys = request.POST.getlist('activity')
        activitys_price = Activity.objects.filter(id__in=activitys)
        suma_a =0
        for a in activitys_price:
            suma_a += a.price
        suma_final = suma_a + suma_p

        t = Treatment.objects.create(name=name, price=suma_final)
        t.activities.set(activitys)
        t.products.set(products)
        return redirect('add_treatment')

class TreatmentView(View):
    def get(self,request):
        treatments = Treatment.objects.all()
        return render(request,'treatments.html', {'treatments': treatments})

class PriceListView(View):

    def get(self,request):
        treats = Treatment.objects.all()

        return render(request,'price_list.html',{'treats': treats})

class TreatmentDetailView(DetailView):
    model = Treatment
    template_name = 'treatment_detail_view.html'
