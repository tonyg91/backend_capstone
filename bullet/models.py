from django.db import models


class Journals(models.Model):
    brand = models.CharField(max_length=100)
    paperweight = models.CharField(max_length=100)
    sizes = models.CharField(max_length=100)
    pages = models.IntegerField(default=3)
    
    
class Supply(models.Model):
    brand = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    ink = models.CharField(max_length=100)
    
class Theme(models.Model):
    image = models.CharField(max_length=300)
    pagelayout = models.CharField(max_length=100)
    creator = models.CharField(max_length=100)