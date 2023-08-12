import os

from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

# Custom user model
class CustomUser(AbstractUser):
#    username = None # Added this after looking up Stackfoverflow
    username = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(_("email address"), unique=True)

    # Specify email as the field to be used as unique identifier
    USERNAME_FIELD = "email"

    # A list of the field names that will be prompted when 
    # creating a superuser via the createsuperuser 
    # management command. This doesn’t have any effect in 
    # other parts of Django like when creating a user in the admin panel.
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

''' Skip image upload capability for now
def get_image_filename(instance, filename):
    name = instance.product.name
    slug = slugify(name)
    return f"products/{slug}-{filename}"
'''

# User profile model - avatar field disabled for now
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
# Disabling profile avatar capability for now
#    avatar = models.ImageField(upload_to=get_image_filename, blank=True)
    bio = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.user.email

'''
    # Disable this profile image capability for now
    @property
    def filename(self):
        return os.path.basename(self.image.name)
'''