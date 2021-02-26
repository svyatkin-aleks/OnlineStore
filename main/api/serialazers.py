from rest_framework import serializers
from ..models import Category, Product


class CategorySerialazer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    slug = serializers.SlugField()

    class Meta():
        model = Category
        fields = ('id', 'name', 'slug')


class ProductSerialazier(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects)
    name = serializers.CharField(required=True)
    slug = serializers.SlugField(required=True)
    image = serializers.ImageField(required=False)
    description = serializers.CharField(required=False)
    price = serializers.DecimalField(max_digits=10, decimal_places=2, required=True)
    stock = serializers.IntegerField(required=True)
    available = serializers.BooleanField(required=True)
    created = serializers.DateTimeField(required=True)

    class Meta():
        model = Product
        fields = ('__all__')

