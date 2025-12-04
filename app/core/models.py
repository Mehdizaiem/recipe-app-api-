"""
Docstring for app.core.models
"""
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
    )


class UserManager(BaseUserManager):
    """
    Docstring for UserManager
    """
    def create_user(self, email, password=None, **extra_fields):
        """
        Docstring for create_user

        :param self: Description
        :param email: Description
        :param password: Description
        :param extra_field: Description
        """
        if not email : 
            raise ValueError('User email not found ')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, password):
        """
        Docstring for create_superuser

        :param self: Description
        :param email: Description
        :param password: Description
        """
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self.db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    """
    Docstring for User
    """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    
    USERNAME_FIELD = 'email'