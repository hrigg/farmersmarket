from django.db import models

class Market(models.Model):
    name= models.CharField(max_length=100)
    day= models.CharField(max_length=100)
    address= models.CharField(max_length=100)
    image= models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']