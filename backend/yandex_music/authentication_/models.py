from django.db import models
from datetime import datetime, timedelta
from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)


from uuid import uuid4
import jwt

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if username is None:
            raise TypeError('Users must have a username')
        
        if email is None:
            raise TypeError('Users must have an email address')
        
        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user
    
    def create_superuser(self, username, email, password):
        if password is None:
            raise TypeError('Superusers must have a password')
        
        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(default=uuid4, primary_key=True)
    username = models.CharField(db_index=True, unique=True, max_length=255)
    email = models.EmailField(db_index=True, unique=True)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = ['username']  

    objects = UserManager()

    def __str__(self) -> str:
        return self.email
    
    @property
    def token(self):
        return self._generate_jwt_token()
    
    def get_full_name(self):
        return self.username
    
    def get_short_name(self):
        return self.username
    
    def _generate_jwt_token(self):
     
        dt = datetime.now() + timedelta(days=1)

        token = jwt.encode({
            'id': str(self.pk),  
            'exp': int(dt.strftime('%s')) 
        }, settings.SECRET_KEY, algorithm='HS256')

        return token