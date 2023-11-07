from django.db import models

# Create your models here.

class Sender(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    EMAIL_BACKEND = models.CharField(max_length=300)
    EMAIL_USE_TLS = models.BooleanField(default=True)
    EMAIL_HOST = models.CharField(max_length=255)
    EMAIL_PORT = models.IntegerField()
    EMAIL_HOST_USER = models.CharField(max_length=255)
    EMAIL_HOST_PASSWORD = models.TextField()
    
    
    

class Category(models.Model):
    name = models.CharField(max_length=255)

    
class Receiver(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    

class ReceiverCategory(models.Model):
    receiver = models.ForeignKey(Receiver, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)    
    
    


class Template(models.Model):
    name = models.CharField(max_length=255)
    design = models.TextField()
    
    

class History(models.Model):
    sender = models.TextField()
    receiver = models.TextField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
