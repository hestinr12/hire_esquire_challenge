from django.contrib import admin

from .models import Job, TimeEntry

# Register your models here.

# create JobAdmin(admin.)


admin.site.register(Job)
admin.site.register(TimeEntry)
