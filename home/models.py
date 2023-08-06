from django.db import models

# makemigrations - create changes and store in a file
# migrate - apply the pending changes created by makemigrations

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name

class Icecream(models.Model):
    img = models.ImageField(upload_to='img')
    desc = models.TextField()
    name = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return self.name