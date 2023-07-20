from django.db import models

# Create your models here.



class drinks( models.Model ):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    price = models.FloatField(null=True, blank=True)
    def __str__(self):
        return self.name[0:50]


class food( models.Model ):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    price = models.FloatField(null=True, blank=True)
    def __str__(self):
        return self.name[0:50]

class dessert( models.Model ):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    price = models.FloatField(null=True, blank=True)
    def __str__(self):
        return self.name[0:50]


