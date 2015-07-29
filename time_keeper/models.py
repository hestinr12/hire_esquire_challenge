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
    
    def __str__(self):
        return self.title

class TimeEntry(models.Model):
    minutes_worked = models.PositiveSmallIntegerField()
    date_stamp = models.DateField()
    work_summary = models.CharField(max_length=300)
    related_job = models.ForeignKey(Job)

