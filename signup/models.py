from django.db import models
from django.contrib.auth.models import User


class Signup(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=200)
    message = models.CharField(max_length=250)

    def __str__(self):
        return self.email