from django.db import models

# Create your models here.
class MembersData(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    paid = models.FloatField(max_length=100)
    def __str__(self):
        return self.name