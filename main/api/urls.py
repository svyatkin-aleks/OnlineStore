from django.urls import path
from .api_views import CategoryListAPIView, CategoryCreateView, CategoryRetrievApiView, CategoryDestroyApiView, ProductListAPIView, ProductCreateAPIView, ProductRetrievApiView, ProductDestroyApiView

urlpatterns = [
    path('categories/list', CategoryListAPIView.as_view(), name='categories'),
    path('categories/create', CategoryCreateView.as_view()),
    path('categories/retriev', CategoryRetrievApiView.as_view()),
    path('categories/destroy', CategoryDestroyApiView.as_view()),
    path('products/list', ProductListAPIView.as_view(), name='products'),
    path('products/create', ProductCreateAPIView.as_view()),
    path('products/retriev', ProductRetrievApiView.as_view()),
    path('products/destroy', ProductDestroyApiView.as_view())
]