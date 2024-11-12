from django.db import models

# Create your models here.

from django.conf import settings
from django.db import models
from django.utils import timezone


class Invoice(models.Model):
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    issued_date = models.DateTimeField(blank=True, null=True)

    def issue(self):
        self.issued_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.id)