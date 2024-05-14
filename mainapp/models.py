from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
GENDER_CHOICE = (
    (None,'Sex'),
    ('M','Male'),
    ('F','Female'),
    
)
class User(AbstractUser):
    address=models.CharField(max_length=100,verbose_name="addressline1")
    number=models.IntegerField(default="100",verbose_name="mobilenumber65")
    gender=models.CharField(choices=GENDER_CHOICE,max_length=2)
