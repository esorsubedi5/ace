from django.urls import path
from . import views
urlpatterns = [
    path('api/product', views.ProductList.as_view()),
    path('api/product/<int:pk>/', views.ProductDetail.as_view(), name='product_detail'),
]
