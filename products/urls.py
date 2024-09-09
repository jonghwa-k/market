from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('', views.ProductListAPIview.as_view(), name='products_list'),
    path('<int:pk>/', views.ProductDetailAPIView.as_view(), name='products_detail'),
]