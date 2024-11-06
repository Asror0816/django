from django.db import models

# Create your models here.


class Kitob(models.Model):
    title = models.CharField(max_length=200)
    published_year = models.IntegerField()
    author = models.CharField(max_length=200)
    description = models.TextField()

    class Kitob(models.Model):
        title = models.CharField(max_length=200)
        published_year = models.IntegerField()
        author = models.CharField(max_length=200)
        description = models.TextField()