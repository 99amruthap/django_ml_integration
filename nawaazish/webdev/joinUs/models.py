from django.db import models

# Create your models here.

class JoinUs(models.Model):
    name = models.CharField(max_length=60, default='Your Name')
    city = models.CharField(max_length=300)
    area = models.CharField(max_length=100)
    pincode = models.PositiveIntegerField()
    phone = models.PositiveIntegerField()
    email = models.EmailField(unique=True)
    insta = models.CharField(max_length=30)
    feedback = models.TextField()

    def __str__(self):
        return self.name




