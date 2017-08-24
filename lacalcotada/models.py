from django.db import models
from django.utils import timezone

# Create your models here.

class Subscrivers(models.Model):
    mail = models.EmailField(primary_key=True)
    name = models.TimeField(max_length=50)
    ip = models.TextField(max_length=20)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.mails
