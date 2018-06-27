from django.db import models
from django.db.models import CharField


# Create your models here.

class Table1(models.Model):
    Text1 = CharField(max_length=100)
    Text2 = CharField(max_length=100)

    def __str__(self):
        return self.Text1
