# Create your models here.
from django.db import models

class Club(models.Model):
    clubName = models.CharField(max_length=201)
    shortName = models.CharField(max_length=200)
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)


class Event(models.Model):
    eventName = models.CharField(max_length=200)
    eventLocation = models.CharField(max_length=200)
    event_date = models.DateTimeField('event first day of competition')
    club = models.ForeignKey(Club)
    list_display = ('eventName', 'event_date')

