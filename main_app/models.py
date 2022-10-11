from django.db import models
from django.contrib.auth.models import User 

class Vendor(models.Model):
    name=models.CharField(max_length=150)
    description= models.TextField(max_length=500)
    website=models.CharField(max_length=150)
    image= models.CharField(max_length=300, default='https://media.istockphoto.com/')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']



class Product(models.Model):
    name= models.CharField(max_length=100)
    price= models.IntegerField(default=1)
    description= models.TextField(max_length=300)
    vendor= models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='products')
    image= models.CharField(max_length=300, default='https://media.istockphoto.com/')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name 

class Market(models.Model):
    name= models.CharField(max_length=100)
    day= models.CharField(max_length=100, default='Saturday')
    times= models.CharField(max_length=100, default='10am-1pm')
    season= models.CharField(max_length=100, default='Memorial Day- Labor Day')
    location= models.CharField(max_length=100)
    image= models.CharField(max_length=300, default='https://media.istockphoto.com/photos/veggie-market-picture-id840320076?s=612x612')
    state=models.CharField(max_length= 5, default='DMV')
    county=models.CharField(max_length= 50, default='Frederick')
    vendors=models.ManyToManyField(Vendor)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

