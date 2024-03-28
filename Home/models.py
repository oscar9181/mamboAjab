from django.db import models

# Create your models here.
class Rentals(models.Model):
    image =models.ImageField(upload_to='images/')
    location = models.CharField(max_length=100,null=True,blank=True)
    house_type = models.CharField(max_length= 50,null=True)
    bedrooms = models.CharField(max_length=10,null=True)
    house_price = models.CharField(max_length= 100,null=True)


class User(models.Model):
    user_name = models.CharField(max_length =100)
    user_email= models.CharField(max_length=100,null=True)
    user_contact= models.CharField(max_length=50,default='')

    


class Properties(models.Model):
    property_name = models.CharField(max_length=150,null=True)
    tenant = models.ForeignKey(User,on_delete=models.CASCADE,null=True)




