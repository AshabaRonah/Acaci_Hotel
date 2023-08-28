from django.db import models

# Create your models here.
class Product(models.Model):
    name= models.CharField(max_length=255)
    image =models.ImageField(default="images/default.png", upload_to="images/")  


    
    def __str__(self):
        return self.name
    
class Contact(models.Model):
    fullname= models.CharField(max_length=255)
    email= models.EmailField()
    phonenumber = models.CharField(max_length=10)
    message = models.TextField(max_length=255)

    def __str__(self):
        return self.fullname

class Signin(models.Model):
    user_email = models.EmailField()
    user_password = models.CharField(max_length=24)

    def __str__(self):
        return self.user_email
    
class Contactus(models.Model):
    Name= models.CharField(max_length=255)
    Email= models.EmailField()
    phonenumber = models.CharField(max_length=10)
    subject  = models.TextField(max_length=255)

    def __str__(self):
        return self.Name