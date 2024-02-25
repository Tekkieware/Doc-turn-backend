from django.db import models

# Create your models here.


from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
 
   


class NewUserManager(UserManager):

    def create_user(self,email,name,password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have an email address')
        
        email = self.normalize_email(email) 
        user = self.model(email=email,name=name) 
        user.set_password(password)
        user.save(using=self.db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = None
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    objects = NewUserManager()
    
    objects = NewUserManager()

    

