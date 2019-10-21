from django.db import models
from apps.logreg.models import *

class MessageManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['message']) < 3:
            errors['length'] = 'Message must be more than 3 characters.'
        return errors

class Message(models.Model):
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    poster = models.ForeignKey(User, related_name='messages')
    likes = models.ManyToManyField(User, related_name='likes')
    objects = MessageManager()

class Comment(models.Model):
    comment = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    poster = models.ForeignKey(User, related_name='comments')
    message = models.ForeignKey(Message, related_name='comments')










# Create your models here.

# EVENT PLANNER

# Have Users be Able to post Events
# Other Users can RSVP events
# Users can post messages on events



class New_User(models.Model):
    full_name = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Event(models.Model):
    event = models.CharField(max_length=200)
    poster = models.ForeignKey(New_User, related_name="event")
    rsvp = models.ManyToManyField(New_User, related_name="user")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Messages(models.Model):
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    poster = models.ForeignKey(New_User, related_name="message")
    event = models.ForeignKey(Event, related_name="message")
    updated_at = models.DateTimeField(auto_now=True)









