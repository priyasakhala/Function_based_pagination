from abc import abstractclassmethod
from operator import mod
from django.db import models

# Create your models here.

class Student(models.Model):
    sid = models.IntegerField()
    sname = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    marks = models.IntegerField()

    def __str__(self):
        return f'{self.sid}--{self.sname}'

class SingleTonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
            self.pk = 1
            super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
            pass

    @classmethod
    def load(cls):
            obj,created = cls.objects.get_or_create(pk=1)
            return obj

class SiteSetting(SingleTonModel):
        site_name = models.CharField(max_length=100)