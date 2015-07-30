import datetime                                                                    
                                                                                   
from django.utils import timezone                                                  
from django.test import TestCase                                                   
from django.core.urlresolvers import reverse                                       
                                                                                   
from time_keeper.models import Job, TimeEntry, unit_string


def create_time_entry(minutes_worked, job):
    return TimeEntry.objects.create(minutes_worked=10, related_job=job, 
        date_stamp=timezone.now())

def create_job(title=''):
    return Job.objects.create(title=title)

class JobMethodTests(TestCase):

    def test_update_total_minutes(self):
        job = create_job()
        job.updateTotalMinutes()
        self.assertEqual(job.total_minutes, 0)
        
        entry = create_time_entry(10, job)
        job.updateTotalMinutes()
        self.assertEqual(job.total_minutes, 10)
        
        entry = create_time_entry(10, job)
        job.updateTotalMinutes()
        self.assertEqual(job.total_minutes, 20)


class JobViewTests(TestCase):
    
    def test_job_list_view_with_no_jobs(self):
        pass

    def test_job_list_view_with_job_no_time_entry(self):
        pass

    def test_job_list_view_with_job_and_time_entry(self):
        pass


class JobFormTests(TestCase):
    
    def test_job_form_fields(self):
        pass


class TimeEntryViewTests(TestCase):

    def test_time_entry_list_view_with_no_time_entrys(self):
        pass

    def test_time_entry_list_view_with_time_entry_no_job(self):
        pass

    def test_time_entry_list_view_with_time_entry_and_job(self):
        pass


class UtilTests(TestCase):
    
    def test_unit_string_singular(self):
        pass

    def test_unit_string_plural(self):
        pass
