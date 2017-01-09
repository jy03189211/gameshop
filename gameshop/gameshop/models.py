from django.db import models

#User can have developed games and purchased games
class User(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True) #if error, probably needs default=timezone.now
    updatedAt = models.DateTimeField(auto_now=True)
    isDeveloper = models.BooleanField()

class Order(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    #Order has purchased games
    orderOfUser = models.ForeignKey(User, on_delete=models.CASCADE)


class Purchase(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    purchaseOfOrder = models.ForeignKey(Order, on_delete=models.CASCADE)

    #Purchase can belong to order or those already purchased by user (relation straight to user)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Game(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    url = models.URLField(max_length=200)
    name = models.CharField(max_length=50)
    price = models.FloatField()
    available = models.BooleanField()
    category = models.CharField(max_length=200)
    #Game has a creator
    createdBy = models.ForeignKey(User,on_delete=models.CASCADE)
    #Game may belong to developed games (relation straight to user) and purchased games
    purchasedGame = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    developedGame = modesl.ForeingKey(User, on_delete=models.CASCADE)

class Savegame(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    data = models.CharField(max_length=200)
    #Savegame belongs to a certain game
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

class Score(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    score = models.PositiveIntegerField()
    #Score belongs to a certain game
    gameScore = models.ForeignKey(Game, on_delete=models.CASCADE)
