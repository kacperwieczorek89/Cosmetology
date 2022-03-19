"""Cosmetology URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cosm_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index.as_view(), name='index'),
    path('producers/', views.ProducerView.as_view(), name='producers'),
    path('add_producer/', views.AddProducerView.as_view(), name='add_producer'),
    path('add_product_type/', views.AddProductTypeView.as_view(), name='add_product_type'),
    path('add_product/', views.AddProductView.as_view(), name='add_product'),
    path('products/', views.ProductView.as_view(), name='products'),
    path('add_activity/', views.AddActivityView.as_view(), name='add_activity'),
    path('activities/', views.ActivityView.as_view(), name='activities'),
    path('add_treatment/', views.AddTreatmentView.as_view(), name='add_treatment'),
    path('treatments/', views.TreatmentView.as_view(), name='treatments'),
    path('price_list/', views.PriceListView.as_view(), name='price_list'),
    path('treatment/<int:pk>/', views.TreatmentDetailView.as_view(), name='treatment_detail_view'),
]
