import pytest
from django.contrib.auth.models import User
from user_interface.models import Product
from admin_interface.models import Collections
from model_bakery import baker
import datetime
from django.contrib import auth
from django.contrib.auth.models import User
import json
from rest_framework.authtoken.models import Token
import time


@pytest.mark.django_db
def test_create_custom():
    """ Create method """

    collection = Collections.objects.create(
        title="asd",
        text="asd",
    )
    assert collection


@pytest.mark.django_db
def test_retrieve_custom():
    """ Retrive method """

    collection = baker.make('admin_interface.Collections')
    queryset = Collections.objects.all()[0]
    assert queryset == collection


@pytest.mark.django_db
def test_update_custom():
    """ Update method """

    collection = baker.make('admin_interface.Collections')
    collection.text = "asd"
    collection.save()
    assert collection


@pytest.mark.django_db
def test_delete_custom():
    """ Delete method """

    collection = baker.make('admin_interface.Collections')
    queryset = Collections.objects.get(id=collection.id)
    queryset.delete()
    assert queryset


# API TESTING

@pytest.mark.django_db
def test_list_collection(api_client):
    endpoint = "/api/v1/admin-interface/collections/"
    baker.make(Collections, _quantity=3)
    api_client = api_client()
    user = User.objects.create(username='legion', password='444444')
    token = Token.objects.create(user=user)
    api_client.force_authenticate(user=user, token=token)
    resp = api_client.get(endpoint)
    assert resp.status_code == 200
    assert len(json.loads(resp.content)) == 3


@pytest.mark.django_db
def test_delete_collection(api_client):
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
    product = Product.objects.create(title='asd', decs='123', price=1)
    resp = api_client.put(endpoint, json.dumps({'title': 'new idea', 'decs': "asd", "price": 1}),
                          content_type='application/json')
    assert resp.status_code == 301
