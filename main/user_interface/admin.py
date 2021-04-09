from django.contrib import admin
from .models import Product, Review, Custom

from django.contrib.admin import DateFieldListFilter


@admin.register(Custom)
class CustomAdmin(admin.ModelAdmin):
    """ Curstom admin Model """

    ordering = ('-created_at',)
    list_display = ('user', 'get_count_of_products')

    class Meta:
        model = Custom
        verbose_name = 'Custom'


admin.site.register(Product)
admin.site.register(Review)
