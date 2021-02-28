from django.urls import path
from .api_views import CategoryListAPIView, CategoryCreateView, CategoryDetailApiView, CategoryDestroyApiView, ProductListAPIView, ProductCreateAPIView, ProductDetailApiView, ProductDestroyApiView

urlpatterns = [
    path('categories/list', CategoryListAPIView.as_view(), name='categories'),
    path('categories/create', CategoryCreateView.as_view()),
    path('categories/detail/<str:id>/', CategoryDetailApiView.as_view()),
    path('categories/destroy', CategoryDestroyApiView.as_view()),
    path('products/list', ProductListAPIView.as_view(), name='products'),
    path('products/create', ProductCreateAPIView.as_view()),
    path('products/detail/<str:id>/', ProductDetailApiView.as_view()),
    path('products/destroy', ProductDestroyApiView.as_view())
]