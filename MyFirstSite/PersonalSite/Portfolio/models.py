from django.db import models
from django.utils import timezone

# Create your models here.

class Contact(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=70,blank = False)
    email= models.EmailField(max_length=50,blank=False)
    number = models.CharField(max_length=17,blank=False)
    date = models.DateTimeField(default=timezone.now)
    desc = models.CharField(max_length=300,blank=True)
    
    
    def __str__(self):
        return self.name