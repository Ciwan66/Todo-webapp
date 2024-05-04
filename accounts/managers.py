from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(self,email,first_name,last_name,password=None,**extra_fields):
        if not email:
            raise ValueError(_("Please Set An Email :D"))
        email = self.normalize_email(email)
        user = self.model(
            email= email,
            first_name = first_name,
            last_name = last_name,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,first_name,last_name,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_("super user must be staff"))
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_("super user must ve superuser"))
        return self.create_user(email,first_name,last_name,password,**extra_fields)

