from django.urls import path
from . import views
# from .views import ProductListAPIview, ProductDetailAPIView
# from .views import ProductDetailAPIView

app_name = 'products'
urlpatterns = [
    path("",views.ProductListAPIView.as_view(), name="product_list"),
    path("<int:pk>/", views.ProductDetailAPIView.as_view(), name="product_detail"),
]