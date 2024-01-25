from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager,PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
# Create your models here.

class UserManager(BaseUserManager):
    
    def create_user(self,email,phonenumber,full_name,password,profile_image=None,**extra_fields):
        if not email:
            raise ValueError("Email cannot not be blank")
        elif not phonenumber:
            raise ValueError("Phone number is a required filed")    
           
        user=self.model(email=email,phonenumber=phonenumber,full_name=full_name,profile_image=profile_image,**extra_fields)
        email=self.normalize_email(email)
        user.set_password(password)
        user.save(using=self._db)
        
    def create_superuser(self,email,phonenumber,full_name,password,profile_image=None,**extra_fields):
        extra_fields.setdefault("is_superuser",True)
        return self.create_user(email=email,phonenumber=phonenumber,full_name=full_name,password=password,profile_image=profile_image,**extra_fields)
        
class User(AbstractUser):
    first_name=None
    last_name=None
    username=None
    email=models.CharField(_("Email"),max_length=50,unique=True)
    phonenumber=models.CharField(_("Phone Number"),max_length=10,blank=False,null=False)
    profile_image=models.ImageField(verbose_name="Profile Image",upload_to="media/profileimage",blank=True,null=True)
    full_name=models.CharField(verbose_name="Full Name",max_length=100,blank=True)
    is_superuser=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=True)
    is_admin=models.BooleanField(default=False)
    last_login=models.DateTimeField(_("Last Login"),default=timezone.now)
    USERNAME_FIELD="email"
    REQUIRED_FIELDS=["phonenumber","full_name"]
    
    objects=UserManager()
    
    
    def __str__(self) -> str:
        return self.email