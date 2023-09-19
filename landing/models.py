from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    city = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.name