import pytest
from django.contrib.auth.models import User
from django.test import Client as WebClient
from cosm_app.models import ProductType,Producer

@pytest.fixture
def client():
    client = WebClient()
    return client

@pytest.fixture
def user():
    x = User(username='kacper2')
    x.set_password('kacper')
    x.save()
    return x

@pytest.fixture
def product_types():
    lst = []
    a = ProductType.objects.create(product_type="Szpatułka", product_type_plural="Szpatułki")
    lst.append(a)
    a = ProductType.objects.create(product_type="Igła",product_type_plural="Igły")
    lst.append(a)
    a = ProductType.objects.create(product_type="Kartridż", product_type_plural="Kartridże")
    lst.append(a)
    return lst

@pytest.fixture
def activities():
    lst = []
    a = ProductType.objects.create(name='strzykanie w kolanie', price=15,time=45,description=';asldfikjashdo;ifj')
    lst.append(a)
    a = ProductType.objects.create(name='strzykanie w kolanie', price=15, time=45, description=';asldfikjashdo;ifj')
    lst.append(a)
    a = ProductType.objects.create(name='strzykanie w kolanie', price=15,time=45,description=';asldfikjashdo;ifj')
    lst.append(a)
    return lst

@pytest.fixture
def product_type():
    a = ProductType.objects.create(product_type='Kartridż', product_type_plural='Kartridże', id=1)
    return a

@pytest.fixture
def producer(product_type):
    a = ProductType.objects.create(name='Andżej', product_types=product_type)
    return a
