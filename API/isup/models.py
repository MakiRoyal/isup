from django.db import models
from django.contrib.auth.models import User


class Domain(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    is_up = models.BooleanField(default=False)
    since = models.DateTimeField()

    def __str__(self):
        return self.name


class Check(models.Model):
    verificationDate = models.DateTimeField()
    is_up = models.BooleanField(default=False)
    message = models.CharField(max_length=255, default="Up")
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)

# Create your models here.
