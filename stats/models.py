from django.db import models
from django.utils import timezone

# Create your models here.


# class Stat(models.Model):
#     author = models.CharField(blank=True, max_length=200, default='anonymous')
#     name = models.CharField(blank=True, max_length=200)
#     tag = models.CharField(blank=True, max_length=1000,)
#     upload = models.FileField(upload_to='')
#
#     def publish(self,author, name, tag, file):
#         self.published_date = timezone.now()
#         self.author = author
#         self.name = name
#         self.tag = tag
#         self.upload.save(name, file)
#         self.save()
#
#
#     def __str__(self):
#         return self.name


class analyz(models.Model):
    title = models.CharField(blank=True, max_length=200)
    author = models.CharField(blank=True, max_length=200)
    genre = models.CharField(blank=True, max_length=200)
    pfr = models.CharField(blank=True, max_length=1000)
    id = models.AutoField(primary_key=True)
    relation = models.IntegerField(blank=True)
    upload = models.FileField(upload_to='')

