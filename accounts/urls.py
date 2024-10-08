from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = 'accounts'
urlpatterns = [
    path('', views.SignUpAPIView.as_view(), name='signup'),
    path('signin/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', views.LoginAPIView.as_view(), name='login'),
    path('<int:pk>/', views.ProFileAPIView.as_view(), name='profile'),
]