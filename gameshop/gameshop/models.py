from django.db import models
from django.utils import timezone
import json
#from django.contrib.postgres.fields import ArrayField

#User can have developed games and purchased games
class User(models.Model):
    #createdAt = models.DateTimeField(default=timezone.now()) #if error, probably needs default=timezone.now
    #updatedAt = models.DateTimeField(default='')
    username = models.CharField(max_length=50,default='user_without_name')
    isDeveloper = models.BooleanField()


class Order(models.Model):
    #createdAt = models.DateTimeField(default=timezone.now())
    #updatedAt = models.DateTimeField(auto_now=True)
    #Order has purchased games
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Purchase(models.Model):
    #createdAt = models.DateTimeField(default=timezone.now())
    #updatedAt = models.DateTimeField(auto_now=True)

    #Purchase can belong to order or those already purchased by user (relation straight to user)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Game(models.Model):
    #createdAt = models.DateTimeField(default=timezone.now())
    #updatedAt = models.DateTimeField(auto_now=True)
    url = models.URLField(max_length=200)
    name = models.CharField(max_length=50)
    price = models.FloatField()
    available = models.BooleanField()

    #category = models.CharField(max_length=200)
    categories = models.CharField(max_length=50, default='')


    #Game has a creator
    createdBy = models.ForeignKey(User,on_delete=models.CASCADE)
    #Game may belong to developed games (relation straight to user) and purchased games
    purchasedGame = models.ForeignKey(Purchase, on_delete=models.CASCADE)

    def setCategories(self, x):
        self.categories = json.dumps(x)

    def getCategories(self):
        print(self.categories)
        return json.loads(self.categories)

class Savegame(models.Model):
    #createdAt = models.DateTimeField(default=timezone.now())
    #updatedAt = models.DateTimeField(auto_now=True)
    data = models.CharField(max_length=200)
    #Savegame belongs to a certain game
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Score(models.Model):
    #createdAt = models.DateTimeField(default=timezone.now())
    #updatedAt = models.DateTimeField(auto_now=True)
    score = models.PositiveIntegerField()
    #Score belongs to a certain game
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
