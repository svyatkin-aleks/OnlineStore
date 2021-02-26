from django.urls import path
from .api_views import CategoryListAPIView, CategoryCreateView, ProductListAPIView, ProductCreateAPIView

urlpatterns = [
    path('categories/list', CategoryListAPIView.as_view(), name='categories'),
    path('categories/create', CategoryCreateView.as_view()),
    path('products/list', ProductListAPIView.as_view(), name='products'),
    path('products/creatr', ProductCreateAPIView.as_view())
]