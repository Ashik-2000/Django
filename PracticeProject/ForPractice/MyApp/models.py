from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=100)
    dept = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=14)
    def __str__(self):
        return self.name