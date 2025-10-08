from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(blank=True)
    profession = models.CharField(max_length=100, blank=True)
    tel_number = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
    
