import pytest
from django.contrib.auth.models import User
from user_interface.models import Product, Review
from model_bakery import baker
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
import json

import datetime


@pytest.mark.django_db
def test_create_reviews():
    """ Create method """

    review = Review.objects.create(
        user=User.objects.create(username='alex', password='123'),
        product=Product.objects.create(
            title='title', decs='decs', price=12
        ),
        text='Text', mark=1
    )
    assert review


@pytest.mark.django_db
def test_retrieve_reviews():
    """ Retrive method """

    review = baker.make('user_interface.Review')
    queryset = Review.objects.all()[0]
    assert queryset == review


@pytest.mark.django_db
def test_update_reviews():
    """ Update method """

    review = baker.make('user_interface.Review')
    review.text = 'Text'
    review.save()
    assert review


@pytest.mark.django_db
def test_delete_reviews():
    """ Delete method """

    review = baker.make('user_interface.Review')
    queryset = Review.objects.get(id=review.id)
    queryset.delete()
    assert queryset


@pytest.mark.django_db
def test_list_reviews():
    """ List method """

    reviews = []
    for i in range(3):
        review = baker.make('user_interface.Review')
        reviews.append(review)

    queryset = Review.objects.all()
    assert list(queryset) == reviews


@pytest.mark.django_db
def test_id_reviews():
    """ Filter by id """

    review = baker.make('user_interface.Review')
    queryset = Review.objects.filter(user=review.user)
    assert list(queryset)[0] == review


@pytest.mark.django_db
def test_created_at_reviews():
    """ Filter by created at """

    review = baker.make('user_interface.Review')
    queryset = Review.objects.filter(created_at=datetime.datetime.now())
    assert review


@pytest.mark.django_db
def test_product_id_reviews():
    """ Filter by product id """
    review = baker.make('user_interface.Review')
    product = Product.objects.create(title='title', decs='decs', price=12)
    queryset = Review.objects.filter(product__id=product.id)
    assert review


# Api Tests
@pytest.mark.django_db
def test_list_product(api_client):
    endpoint = "/api/v1/user-interface/reviews/"
    baker.make(Review, _quantity=3)
    api_client = api_client()
    user = User.objects.create(username='legion', password='444444')
    token = Token.objects.create(user=user)
    api_client.force_authenticate(user=user, token=token)
    resp = api_client.get(endpoint)
    assert resp.status_code == 200
    assert len(json.loads(resp.content)) == 3


@pytest.mark.django_db
def test_delete_collection(api_client):
    endpoint = "/api/v1/user-interface/reviews/1"
    api_client = api_client()
    user = User.objects.create(username='legion', password='444444')
    token = Token.objects.create(user=user)
    api_client.force_authenticate(user=user, token=token)
    resp = api_client.delete(endpoint)
    assert resp.status_code == 301


# Update method
@pytest.mark.django_db
def test_update_product(api_client):
    endpoint = "/api/v1/user-interface/reviews/1"
    api_client = api_client()
    user = User.objects.create(username='legion', password='444444')
    token = Token.objects.create(user=user)
    api_client.force_authenticate(user=user, token=token)
    data = {"title": "asda", "decs": "asd", "price": 1}
    resp = api_client.put(endpoint, json.dumps({'title': 'new idea', 'decs': "asd", "price": 1}),
                          content_type='application/json')
    assert resp.status_code == 301
