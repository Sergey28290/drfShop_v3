from django_filters import rest_framework as filters, CharFilter

from .models import Product, Review, Custom


class ProductFilter(filters.FilterSet):
    """ Product Filter """

    price = filters.RangeFilter()
    
    title = filters.ModelMultipleChoiceFilter(
        field_name="title",
        to_field_name="title",
        queryset=Product.objects.all(),
    )

    decs = filters.ModelMultipleChoiceFilter(
        field_name="decs",
        to_field_name="decs",
        queryset=Product.objects.all(),
    )

    class Meta:
        model = Product
        fields = ("price", "title", 'decs')


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    """ Char Filter 
    
    this class is needed to create
    model fields in filter fields
    """
    pass


class ReviewFilter(filters.FilterSet):
    """ Review Filter """

    user_id = CharFilterInFilter(
        field_name="user__id",
        lookup_expr='in'
    )

    created_at = filters.ModelMultipleChoiceFilter(
        field_name='created_at',
        to_field_name='created_at',
        queryset=Review.objects.all()
    )

    product_id = CharFilterInFilter(
        field_name="product_id__id",
        lookup_expr='in'
    )

    class Meta:
        model = Review
        fields = ('user_id', 'created_at', 'product_id')


class CustomFilter(filters.FilterSet):
    """ Custom Filter """

    price = filters.RangeFilter()
    created_at = filters.RangeFilter() 
    updated_at = filters.RangeFilter()    
    product = CharFilter(field_name='product__title', lookup_expr='icontains')

    class Meta:
        model = Custom
        fields = ('price', 'created_at', 'updated_at', 'product')        
