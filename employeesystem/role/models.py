from django.db import models
from right.models import Rights
# Create your models here.
class Roles(models.Model):
    role = models.CharField(max_length=150, unique=True)
    rights = models.ManyToManyField(Rights, blank=True)
    def __str__(self):
        return self.role