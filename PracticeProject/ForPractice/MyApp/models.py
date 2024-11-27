from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.TextField(max_length=100)
    dept = models.TextField(max_length=100)
    email = models.EmailField()
    phone = models.TextField(max_length=100)
    def __str__(self):
        return self.name