from .models import Job, TimeEntry
from django.forms import ModelForm, HiddenInput


class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = [
            'title',
        ]


class TimeEntryForm(ModelForm):
    class Meta:
        model = TimeEntry
        fields = [
            'work_summary',
            'date_stamp',
            'minutes_worked',
            'related_job',
        ]
