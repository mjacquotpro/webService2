from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Film(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=2048)
    release_date = models.DateField()
    rating = models.IntegerField(blank=True, null=True, choices=[(i, i) for i in range(6)])
    categories = models.ManyToManyField(Category, related_name='films')
    poster = models.ImageField(upload_to='posters/', null=True, blank=True)

    def __str__(self):
        return self.name
