from django.db import models
from django.contrib.auth.models import User


class Game(models.Model): # A topic the user is learning about.
    ID_game = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length = 200)
    description = models.TextField()

    def __str__(self): # Return a string representation of the model.
        return self.name
    
class Rental(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    rental_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)

    def _str_(self):
        return f"{self.user.username} rented {self.game.name}"
    
class Return(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    return_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} returned {self.game.title} on {self.return_date}"
    
