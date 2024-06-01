from django.db import models

class Advert(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    img = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    place = models.CharField(max_length=100)
    user_id = models.IntegerField()
