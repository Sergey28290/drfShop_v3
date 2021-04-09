import pytest
from django.contrib.auth.models import User
from user_interface.models import Custom, Product
from model_bakery import baker
import datetime
from django.contrib.auth.models import User
from django.contrib.auth.models import User
import json
from rest_framework.authtoken.models import Token
import time


@pytest.mark.django_db
def test_create_custom():
    """ Create method """

    custom = Custom.objects.create(
        user=User.objects.create(username='Alex', password='123'),
        status='NW', price=0
    )
    assert custom


@pytest.mark.django_db
def test_retrieve_custom():
    """ Retrive method """

    custom = baker.make('user_interface.Custom')
    queryset = Custom.objects.all()[0]
    assert queryset == custom


@pytest.mark.django_db
def test_update_custom():
    """ Update method """

    custom = baker.make('user_interface.Custom')
    custom.price = 12
    custom.save()
    assert custom


@pytest.mark.django_db
def test_delete_custom():
    """ Delete method """

    custom = baker.make('user_interface.Custom')
    queryset = Custom.objects.get(id=custom.id)
    queryset.delete()
    assert queryset


@pytest.mark.django_db
def test_price_filter_custom():
    """ Filter by price """

    custom = baker.make('user_interface.Custom')
    queryset = Custom.objects.filter(price=custom.price)
    assert list(queryset)[0] == custom


@pytest.mark.django_db
def test_created_at_filter():
    """ Filter by created_at """

    custom = baker.make('user_interface.Custom')
    queryset = Custom.objects.filter(created_at=datetime.datetime.now())
    assert custom


@pytest.mark.django_db
def test_updated_at_filter():
    """ Filter by updated_at """

    custom = baker.make('user_interface.Product')
    queryset = Custom.objects.filter(updated_at=custom.updated_at)
    assert custom


@pytest.mark.django_db
def test_product_filter():
    """ Filter by product """

    custom = baker.make('user_interface.Custom')
    product = Product.objects.create(title='title', decs='decs', price=12)
    queryset = Custom.objects.filter(product__id=product.id)
    assert custom


# API TESTING
@pytest.mark.django_db
def test_list_custom(api_client):
    endpoint = "/api/v1/user-interface/custom/"
    baker.make('user_interface.Custom')
    api_client = api_client()
    user = User.objects.create(username='legion', password='444444')
    token = Token.objects.create(user=user)
    api_client.force_authenticate(user=user, token=token)
    resp = api_client.get(endpoint)
    assert resp.status_code == 200
    assert len(json.loads(resp.content)) == 1


@pytest.mark.django_db
def test_delete_custom(api_client):
    endpoint = "/api/v1/user-interface/custom/1"
    api_client = api_client()
    user = User.objects.create(username='legion', password='444444')
    token = Token.objects.create(user=user)
    api_client.force_authenticate(user=user, token=token)
    resp = api_client.delete(endpoint)
    assert resp.status_code == 301


# Update method
@pytest.mark.django_db
def test_update_product(api_client):
    endpoint = "/api/v1/user-interface/custom/1"
    api_client = api_client()
    user = User.objects.create(username='legion', password='444444')
    token = Token.objects.create(user=user)
    api_client.force_authenticate(user=user, token=token)
    product = Product.objects.create(title='asd', decs='123', price=1)
    custom = Custom.objects.create(user=user, status="NEW", price=1, id=1)
    resp = api_client.put(endpoint, json.dumps({'title': 'new idea', 'decs': "asd", "price": 1}),
                          content_type='application/json')
    assert resp.status_code == 301