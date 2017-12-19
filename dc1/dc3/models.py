from django.db import models
from django.conf import settings
import datetime
from django.utils import timezone
from django.template.defaultfilters import slugify
# Create your models here.
class Pet(models.Model):
    
    species = models.CharField(max_length=10)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    name = models.CharField(max_length=50)
    birthday = models.DateField(auto_now=False, auto_now_add=False)
    slug = models.SlugField(editable=False)

    def __str__(self):
        return self.name

    
    

    
