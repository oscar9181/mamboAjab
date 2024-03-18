from django.db import models


class Rentals(models.Model):
    image =models.ImageField((""), upload_to=None, height_field=None, width_field=None, max_length=None)
    location = models.CharField(max_length=100,null=True,blank=True)
    house_type = models.CharField(max_length= 50,null=True)
    bedrooms = models.CharField(max_length=10,null=True)
    house_price = models.CharField(max_length= 100,null=True)
    location = models.CharField(max_length=100,null=True,blank=True)


class User(models.Model):
    user_name = models.CharField(max_length =100)
    user_email= models.CharField(max_length=100,null=True)
    user_contact= models.CharField(max_length=50,default='')
    


class Properties(models.Model):
    property_name = models.CharField(max_length=100,null=True)
    tenant = models.ForeignKey(User,on_delete=models.CASCADE,null=True)




# Create your models here.