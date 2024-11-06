from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    author = models.CharField(max_length=100, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    show_counter = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return  str(self.year) + ' ' + self.title

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        ordering = ['id']