import datetime
import uuid

from django.db import models
from django.utils import timezone

# Create your models here.

class Job(models.Model):                                                           
    # id taken from docs.djangoproject.com/en/1.8/ref/models/fields/#uuidfield  
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    title = models.CharField(max_length=140)                                       
    total_minutes = models.PositiveIntegerField(default=0)
    
    def updateTotalMinutes(self):
        self.total_minutes = 0
        for entry in self.timeentry_set.all():
            self.total_minutes += entry.minutes_worked
        self.save()

    def __str__(self):
        unit = unit_string(self.total_minutes, 'minute')
        return "{} - {} {}".format(self.title, self.total_minutes, unit)


class TimeEntry(models.Model):
    minutes_worked = models.PositiveSmallIntegerField()
    date_stamp = models.DateField()
    work_summary = models.CharField(max_length=300)
    related_job = models.ForeignKey(Job)
    
    def __str__(self):
        unit = unit_string(self.minutes_worked, 'minute')
        return "{}: {} {} on {}".format(
            self.work_summary,
            self.minutes_worked,
            unit,
            self.date_stamp)


def unit_string(count, string):
    """Naive pluaralize..."""
    return  string if count == 1 else "{}s".format(string)
