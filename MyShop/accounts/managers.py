from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db import models


class UserManager(BaseUserManager):

    def create_user(self, username, phone_number, email, full_name, password=None):
        if not username:
            return ValueError('please add your UserName')
        if not phone_number:
            return ValueError('please add your Phone Number')
        if not email:
            return ValueError('please add your Email')
        if not full_name:
            return ValueError('please add your Full Name')

        normalize_email =self.normalize_email(email)
        user = self.model(
            username=username,
            phone_number=phone_number,
            email=normalize_email,
            full_name=full_name
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, phone_number, email, full_name, password):
        user = self.create_user(username, phone_number, email, full_name, password)
        user.is_admin = True
        user.save(using=self._db)
        return user

