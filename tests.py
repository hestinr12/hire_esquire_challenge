import datetime                                                                    
                                                                                   
from django.utils import timezone                                                  
from django.test import TestCase                                                   
from django.core.urlresolvers import reverse                                       
                                                                                   
from .models import Job, TimeEntry, unit_string


class JobMethodTests(TestCase):

    def test_update_total_minutes_on_time_entry_create(self):
        pass

    def test_update_total_minutes_on_time_entry_delete(self):
        pass

    def test_update_total_minutes_on_time_entry_update(self):
        pass


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
