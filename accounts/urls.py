from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.SignUpAPIView.as_view(), name='signup'),
]