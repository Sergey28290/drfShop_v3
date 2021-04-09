from django.db import models
from user_interface.models import Product


class Collections(models.Model):
	''' Collections model '''

	title = models.CharField(verbose_name='Title', max_length=50)
	text = models.TextField(verbose_name='Text')
	product = models.ManyToManyField(Product, verbose_name='Product')
	created_at = models.DateTimeField(verbose_name='Created_at', auto_now_add=True)
	updated_at = models.DateTimeField(verbose_name='Updated_at', auto_now=True)

	def __str__(self):
		return self.title
