import pytest
from django.test import TestCase , Client as Webclient
from cosm_app.models import Activity,ProductType,Producer

from django.urls import reverse

@pytest.mark.django_db
class TestViews:
    def test_index(self, client,user):
        url = reverse('index')
        response = client.get(url)
        assert response.status_code == 302
        url = reverse('add_producer')
        client.force_login(user)
        response = client.get(url)
        assert response.status_code == 200


    def test_activities(self, client):
        url = reverse('activities')
        response = client.get(url)
        assert response.status_code == 200

    def test_price_list(self, client):
        url = reverse('price_list')
        response = client.get(url)
        assert response.status_code == 200

    def test_products(self, client):
        url = reverse('products')
        response = client.get(url)
        assert response.status_code == 200

    def test_add_producer_view_without_login(self, client):
        url = reverse('add_producer')
        response = client.get(url)
        assert response.status_code == 200

    def test_add_producer_view_withour_login_2(self, client,user):
        url = reverse('add_producer')
        client.force_login(user)
        response = client.get(url)
        assert response.status_code == 200

    def test_treatment_detail_view(self,client):
        # url = reverse('treatment_detail_view')
        # response = client.get(url)
        # assert response.status_code == 200
        assert True

    def test_treatments_view(self,client):
        url = reverse('treatments')
        response = client.get(url)
        assert response.status_code == 200

    def test_login_view(self, client, user):
        dct = {
            'username': 'kacper2',
            'password': 'kacper'
        }
        url = reverse('login')
        response = client.post(url, dct)
        assert response.wsgi_request.user.is_authenticated

@pytest.mark.django_db
class TestAdds:
    def test_add_product_type(self, client):
        dct = {
            'product_type': 'śmierdzidło',
            'product_type_plural': 'śmierdzidła'
        }
        url = reverse('add_product_type')
        response = client.post(url, dct)
        assert ProductType.objects.get(**dct)



    def test_add_activity(self, client):
        dct = {
            'name': 'śmierdzidło',
            'price': '15.00',
            'time': '45',
            'description':'iuyuiyfgyuifgyuig'
        }
        url = reverse('add_activity')
        response = client.post(url, dct)
        assert Activity.objects.get(**dct)




@pytest.mark.django_db
def test_add_producer(client, product_type):
        dct = {
            'name': 'ANDŻEJ',
            'product_types': str(product_type.id),
        }
        url = reverse('add_producer')
        response = client.post(url, dct)
        assert Producer.objects.first()