from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, username, password):
        if not username:
            raise ValueError('The Username field must be set')
        
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True, primary_key=True)
    password = models.CharField(max_length=100)
    
    objects = UserManager()

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username