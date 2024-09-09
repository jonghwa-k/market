from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime

class User(AbstractUser):
    email = models.EmailField(unique=True, null=False, blank=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    birthday = models.DateField(default=datetime.date.today, null=False, blank=False)
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
        ('X', 'Prefer not to say')  # 선택하지 않음
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='X', null=True, blank=True)
    bio = models.CharField(max_length=30, null=True, blank=True)

    # username과 email을 기반으로 로그인할 수 있도록 설정
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name', 'birthday']

    def __str__(self):
        return self.username


