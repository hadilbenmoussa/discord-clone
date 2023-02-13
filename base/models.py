from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    # setting the textfield parameter to true means it can't be blank
    # the database cannot have an instance of this model that is blank
    description = models.TextField(null=True, blank=True)
    # to store the users in a room
    participants = models.ManyToManyField(
        User, related_name='paticipants', blank=True)
    # when the model is updated
    updated = models.DateTimeField(auto_now=True)
    # when the room was created
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # we need to establish a foreignkey cause we have 1-N relationship room - message
    # we use on_delete= models.CASCADE to specify when a room is deleted what we must delete all the messages attached to this room
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50]
