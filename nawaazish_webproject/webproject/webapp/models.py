from django.db import models

# Create your models here.

class JoinUs(models.Model):
    name = models.TextField(max_length=60)
    city = models.TextField(max_length=300)
    area = models.TextField(max_length=100)
    pincode = models.TextField(max_length=6)
    phone = models.TextField(max_length=10)
    email = models.TextField(unique=True)
    insta = models.TextField(max_length=30)

    def __str__(self):
        return self.name


class ContactUs(models.Model):
    name = models.TextField()
    email = models.TextField()
    subject = models.TextField()
    message = models.TextField()

    def __str__(self):
        return self.name

