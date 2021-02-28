from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView
from .serialazers import CategorySerialazer, ProductSerialazier
from ..models import Category, Product
from rest_framework.filters import SearchFilter


class CategoryListAPIView(ListAPIView):
    serializer_class = CategorySerialazer
    queryset = Category.objects.all()


class CategoryCreateView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerialazer


class CategoryDetailApiView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerialazer
    lookup_field = 'id'


class CategoryDestroyApiView(DestroyAPIView):
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


class ProductDetailApiView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = CategorySerialazer
    lookup_field = 'id'


class ProductDestroyApiView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = CategorySerialazer

