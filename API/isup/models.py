from django.db import models

class Domain(models.Model):
    name = models.CharField(max_length=100)
    is_up = models.BooleanField(default=False)
    since = models.DateTimeField(auto_now_add=True)

class Check(models.Model):
    verificationDate = models.DateTimeField(auto_now_add=True)
    is_up = models.BooleanField(default=False)
    message = models.CharField(max_length=100, default="Up")
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)

# Create your models here.
