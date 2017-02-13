from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import CharField, Form, PasswordInput
from django.utils import timezone
from django.contrib.auth.models import User
import base64, binascii, hashlib, json, os, pprint


"""
NOTE: the created_at and updated_at probably will not show up in the admin panel
when implemented with the auto_now and auto_now_add, because Django.
http://stackoverflow.com/a/1737078/1425689
"""

class User(AbstractUser):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(auto_now=True, null=True)
    username = models.CharField(
        max_length=50, default='user_without_name', unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100, default="",)
    is_developer = models.BooleanField(default=False)
    public_name = models.CharField(max_length=50, default="")
    # authenticating api requests
    api_hosts = models.CharField(max_length=512, default="*", blank=True)
    api_key = models.CharField(
        max_length=512, null=True, blank=True, unique=True)

    def generate_api_key(self):
        random_material = binascii.hexlify(os.urandom(24))
        hash_key = hashlib.sha256(random_material)
        self.api_key = base64.b64encode(self.username + '::' + hash_key)

    def get_api_host_list(self):
        return [h.strip() for h in self.api_hosts.split(',')]

    # override save to default an empty 'public_name' with 'username'
    def save(self, *args, **kwargs):
        if not self.public_name:
            self.public_name = self.username
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.username


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name.capitalize()


class Game(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    url = models.URLField(max_length=200)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500, null=True, blank=True)
    price = models.FloatField()
    available = models.BooleanField(default=False)
    created_by = models.ForeignKey(
        User, related_name='developed_games', on_delete=models.CASCADE)
    # a game can be owned by multiple users
    owned_by = models.ManyToManyField(User, related_name='owned_games')
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    category = models.ForeignKey(Category, null=True, blank=True)

    # TODO: add release_date and change that into the template also

    def __str__(self):
        return self.name


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_ref = models.CharField(max_length=256)

    @property
    def total(self):
        total = 0
        for purchase in self.purchases.all():
            total += purchase.game.price
        return total

    def __str__(self):
        return 'Order {} ({})'.format(self.pk, self.user.username)


class Purchase(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    game = models.ForeignKey(Game, related_name='purchases', on_delete=models.CASCADE)
    order = models.ForeignKey(Order, related_name='purchases', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.FloatField()

    def __str__(self):
        return 'Purchase {} ({})'.format(self.pk, self.user.username)


class Savegame(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    data = models.CharField(max_length=512)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='savegames', on_delete=models.CASCADE)

    def __str__(self):
        return 'Savegame ({}, {})'.format(self.game, self.user.username)


class Score(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    score = models.PositiveIntegerField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return 'Score ({}, {}, {})'.format(
            self.score, self.game, self.user.username)
