from django.db import models
# 유저모델을 바꿀 때 상속받는 모델(?)
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    nickname = models.CharField(max_length = 100)
    phone_number = models.CharField(max_length = 100, blank = True)
    e_mail = models.CharField(max_length = 100)
    bio = models.TextField(blank=True)
    profile = models.ImageField(blank=True, upload_to="media/images/%Y/%m")