from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    #foreign class(Agent) should come first, to be recognized
    # OR
    #agent = models.ForeignKey("Agent", on_delete) 
    #"Agent" tells Django that class Agent is in this file




