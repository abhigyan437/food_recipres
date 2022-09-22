from django.db import models

# Create your models here.
class Recipes(models.Model):
    recipe_name = models.CharField(max_length=200)
    recipe_description = models.TextField()

    def __str__(self):
        return self.recipe_name

class Users(models.Model):
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.name
