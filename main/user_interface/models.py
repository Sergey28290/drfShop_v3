from django.db import models

from django.contrib.auth.models import User


class Product(models.Model):
    """ Product model """

    title = models.CharField(verbose_name='Title', max_length=50)
    decs = models.TextField(verbose_name='Desc')
    price = models.PositiveIntegerField(verbose_name='Price', default=0)
    created_at = models.DateTimeField(verbose_name='Created_at', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Updated_at', auto_now=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    """ Review model """

    REVIEW_MARKS = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    )

    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE, unique=False)
    product = models.ForeignKey(Product, verbose_name='Product', on_delete=models.CASCADE, null=True, unique=False)
    text = models.TextField(verbose_name='Text')
    mark = models.PositiveIntegerField(verbose_name='Mark', default=0, choices=REVIEW_MARKS)
    created_at = models.DateTimeField(verbose_name='Created_at', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Updated_at', auto_now=True)

    def __str__(self):
        return f"{self.created_at}"


class Custom(models.Model):
    """ Custom model """

    Custom_STATUS = (
        ('NW', 'NEW'),
        ("IP", "IN_PROGRESS"),
        ("DN", "DONE")
    )

    user = models.OneToOneField(User, verbose_name='User', on_delete=models.CASCADE)
    product = models.ManyToManyField(Product, verbose_name='Product')
    status = models.CharField(verbose_name='Status', max_length=50, choices=Custom_STATUS)
    price = models.PositiveIntegerField(verbose_name='Price', default=0)
    created_at = models.DateTimeField(verbose_name='Created_at', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Updated_at', auto_now=True)

    def get_count_of_products(self):
        """ Method for getting count of products in custom """

        return len(self.product.all())

    def as_json(self):
        """ Method for getting info in json """

        return dict(
            user=self.user, product=self.product,
            status=self.status,
            created_at=self.created_at.isoformat(),
            updated_at=self.updated_at.isoformat(),
            price=self.price)

    def __str__(self):
        return self.status
