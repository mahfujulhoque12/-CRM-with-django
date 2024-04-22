from django.db import models

# Create your models here.

class Record(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    frist_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    provience = models.CharField(max_length=150)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.frist_name + "   " + self.last_name

