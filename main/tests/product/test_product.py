import pytest
from django.contrib.auth.models import User
from user_interface.models import Product
from model_bakery import baker
from rest_framework.authtoken.models import Token
import json


@pytest.mark.django_db
def test_create_product():
    """ Create method """

    product = Product.objects.create(title='title', decs='decs', price=0)
    assert product


@pytest.mark.django_db
def test_retrieve_product():
    """ Retrive method """

    customer = baker.make('user_interface.product')
    queryset = Product.objects.all()[0]
    assert queryset == customer


@pytest.mark.django_db
def test_update_product():
    """ Update method """

    product = baker.make('user_interface.Product')
    product.title = 'Title'
    product.save()
    assert product


@pytest.mark.django_db
def test_delete_product():
    """ Delete method """

    product = baker.make('user_interface.Product')
    queryset = Product.objects.get(id=product.id)
    queryset.delete()
    assert queryset


@pytest.mark.django_db
def test_list_courses():
    """ List method """

    products = []
    for i in range(3):
        product = baker.make('user_interface.Product')
        products.append(product)

    queryset = Product.objects.all()
    assert list(queryset) == products


@pytest.mark.django_db
def test_price_filter():
    """ Filter by price """

    product = baker.make('user_interface.Product')
    queryset = Product.objects.filter(price=product.price)
    assert list(queryset)[0] == product


@pytest.mark.django_db
def test_title_filter():
    """ Filter by title """

    product = baker.make('user_interface.Product')
    queryset = Product.objects.filter(title=product.title)
    assert list(queryset)[0] == product


@pytest.mark.django_db
def test_desc_filter():
    """ Filter by decs """

    product = baker.make('user_interface.Product')
    queryset = Product.objects.filter(decs=product.decs)
    assert list(queryset)[0] == product


# API Test

@pytest.mark.django_db
def test_list_product(api_client):
    endpoint = "/api/v1/user-interface/products/"
    baker.make(Product, _quantity=3)
    api_client = api_client()
    user = User.objects.create(username='legion', password='444444')
    token = Token.objects.create(user=user)
    api_client.force_authenticate(user=user, token=token)
    resp = api_client.get(endpoint)
    assert resp.status_code == 200
    assert len(json.loads(resp.content)) == 3


@pytest.mark.django_db
def test_delete_product(api_client):
    endpoint = "/api/v1/user-interface/products/1"
    api_client = api_client()
    user = User.objects.create(username='legion', password='444444')
    token = Token.objects.create(user=user)
    api_client.force_authenticate(user=user, token=token)
    resp = api_client.delete(endpoint)
    assert resp.status_code == 301


# Update method
@pytest.mark.django_db
def test_update_product(api_client):
    endpoint = "/api/v1/user-interface/products/1"
    api_client = api_client()
    user = User.objects.create(username='legion', password='444444')
    token = Token.objects.create(user=user)
    api_client.force_authenticate(user=user, token=token)
    data = {"title": "asda", "decs": "asd", "price": 1}
    resp = api_client.put(endpoint, json.dumps({'title': 'new idea', 'decs': "asd", "price": 1}),
                          content_type='application/json')
    assert resp.status_code == 301
