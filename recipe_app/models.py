from django.db import models

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image_url = models.URLField()
    cooking_time = models.PositiveIntegerField()
    preparation_time = models.PositiveIntegerField()
    ingredients = models.ManyToManyField('Ingredient')

    def __str__(self):
        return self.title

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name