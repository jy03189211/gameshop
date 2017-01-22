from django.db import models
from django.utils import timezone
import json

"""
NOTE: the created_at and updated_at probably will not show up in the admin panel
when implemented with the auto_now and auto_now_add, because Django.
http://stackoverflow.com/a/1737078/1425689
"""

class User(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    username = models.CharField(max_length=50, default='user_without_name')
    public_name = models.CharField(max_length=50, null=True, blank=True)
    is_developer = models.BooleanField()


class Game(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    url = models.URLField(max_length=200)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250, null=True, blank=True)
    price = models.FloatField()
    available = models.BooleanField(default=False)
    categories = models.CharField(max_length=50, default='')
    created_by = models.ForeignKey(User, related_name='developed_games', on_delete=models.CASCADE)
    # a game can be owned by multiple users
    owned_by = models.ManyToManyField(User, related_name='owned_games')

    def set_categories(self, x):
        self.categories = json.dumps(x)

    def get_categories(self):
        print(self.categories)
        return json.loads(self.categories)


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Purchase(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    game = models.ForeignKey(Game, related_name='purchases', on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Savegame(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    data = models.CharField(max_length=512)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='savegames', on_delete=models.CASCADE)


class Score(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    score = models.PositiveIntegerField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
