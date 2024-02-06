from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin

'''Creating custom user registration model'''

class UserProfileManager(BaseUserManager):
    def create_user(self,email,first_name,last_name,password = None):
        if not email:
            raise ValueError('Please Provide Email')
        ne = self.normalize_email(email)
        upo = self.model(email = ne,first_name = first_name,last_name = last_name)
        upo.set_password(password)
        upo.save()
        return upo
    def create_superuser(self,email,first_name,last_name,password):
        upo = self.create_user(email,first_name,last_name,password)
        upo.is_staff = True
        upo.is_superuser = True
        upo.save()

class UserProfile(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(primary_key = True)
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False)
    objects = UserProfileManager()  # we are creating object of parent class and connecting here
    USERNAME_FIELD = 'email'        # instead of authorizing using username, we are performing using email
    REQUIRED_FIELDS = ['first_name','last_name'] 

    ''' 
        After that register into admin.py
    
        go to settings.py and write the AUTH_USER_MODEL = "app.UserProfile"  means class name.

        now do makemigrations and then migrate

        if you do 1st migrate it will take built in user model, 
        to avoid that, and to consider our custom usermodel please skip the 1st python manage.py migrate
        
    '''
