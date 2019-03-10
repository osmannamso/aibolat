from datetime import datetime

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)
    parent = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True, default=None)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=20)
    avatar = models.TextField()

    def __str__(self):
        return self.name


class New(models.Model):
    title = models.CharField(max_length=30)
    date = models.DateTimeField(default=datetime.now, blank=True)
    context = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    categories = models.ManyToManyField(Category, related_name='rubricks')

    def __str__(self):
        return self.title
