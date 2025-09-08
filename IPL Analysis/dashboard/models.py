from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100)
    matches_played = models.IntegerField()
    wins = models.IntegerField()
    losses = models.IntegerField()
    win_percentage = models.FloatField()

    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    matches_played = models.IntegerField()
    runs = models.IntegerField()
    wickets = models.IntegerField()
    average = models.FloatField()

    def __str__(self):
        return self.name

class Match(models.Model):
    date = models.DateField()
    team1 = models.CharField(max_length=100)
    team2 = models.CharField(max_length=100)
    winner = models.CharField(max_length=100)
    margin = models.IntegerField()
    venue = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.team1} vs {self.team2} on {self.date}"
