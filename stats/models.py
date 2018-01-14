from django.db import models
from django.utils import timezone

# Create your models here.


class Stat(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=200)
    tag = models.CharField(max_length=1000)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name
    