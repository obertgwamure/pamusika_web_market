from django.db import models
from django.contrib.auth.models import User

# Creating models for items.

class Category(models.Model):
    name = models.CharField(max_length=255)

    # setting up class name plural
    class Meta:
        verbose_name_plural = 'Categories'
        # setting objects to be ordered by name
        ordering = ('name',)

    # setting up object name to return self.name
    def __str__(self):
        return self.name

class Item(models.Model):
    # linking the item to a category from the database.
    # on_delete modles.CASCADE means all items are deleted when the creator is deleted.
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField(default=0.00)
    image = models.ImageField(upload_to='static/images',blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    # linking the item to a user from the user database.
    # on_delete modles.CASCADE means all items are deleted when the creator is deleted.
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    # setting up object name to return self.name
    def __str__(self):
        return self.name


