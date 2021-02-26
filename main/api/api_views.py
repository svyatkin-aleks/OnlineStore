from rest_framework.generics import ListAPIView, CreateAPIView
from .serialazers import CategorySerialazer, ProductSerialazier
from ..models import Category, Product
from rest_framework.filters import SearchFilter


class CategoryListAPIView(ListAPIView):
    serializer_class = CategorySerialazer
    queryset = Category.objects.all()


class CategoryCreateView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerialazer


class ProductListAPIView(ListAPIView):
    serializer_class = ProductSerialazier
    queryset = Product.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['price', 'name']


class ProductCreateAPIView(CreateAPIView):
    serializer_class = ProductSerialazier
    queryset = Product.objects.all()
