import datetime                                                                    
                                                                                   
from django.utils import timezone                                                  
from django.test import TestCase                                                   
from django.core.urlresolvers import reverse                                       
                                                                                   
from time_keeper.models import Job, TimeEntry, unit_string


def create_time_entry(minutes_worked, job, work_summary):
    return TimeEntry.objects.create(minutes_worked=10, related_job=job, 
        date_stamp=str(timezone.now()).split(" ")[0], 
        work_summary=work_summary)

def create_job(title=''):
    return Job.objects.create(title=title)

class JobMethodTests(TestCase):

    def test_update_total_minutes(self):
        job = create_job()
        job.updateTotalMinutes()
        self.assertEqual(job.total_minutes, 0)
        
        entry = create_time_entry(10, job, "")
        job.updateTotalMinutes()
        self.assertEqual(job.total_minutes, 10)
        
        entry = create_time_entry(10, job, "")
        job.updateTotalMinutes()
        self.assertEqual(job.total_minutes, 20)


class JobViewTests(TestCase):
    
    def test_job_list_view_with_no_jobs(self):
        response = self.client.get(reverse('time_keeper:job_index'))
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "<td>")
        self.assertQuerysetEqual(response.context['jobs'], [])

    def test_job_list_view_with_job_no_time_entry(self):
        job = create_job(title="test title")
        response = self.client.get(reverse('time_keeper:job_index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "test title")
        self.assertQuerysetEqual(response.context['jobs'], 
            ["<Job: {}>".format(str(job))])

    def test_job_list_view_with_job_and_time_entry(self):
        job = create_job(title="test title")
        response = self.client.get(reverse('time_keeper:job_index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "test title")
        self.assertQuerysetEqual(response.context['jobs'], 
            ["<Job: {}>".format(str(job))])
   
    def test_job_read_view(self):
        job = create_job(title="test title")
        response = self.client.get(reverse('time_keeper:job_detail', 
            args=[job.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "test title")
    
    def test_job_update_view_get(self):
        job = create_job(title="test title")
        response = self.client.get(reverse('time_keeper:job_update', 
            args=[job.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "test title")
    
    def test_job_delete_view_get(self):
        job = create_job(title="test title")
        response = self.client.get(reverse('time_keeper:job_delete',
            args=[job.id]), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "test title")


class JobFormTests(TestCase):
    
    def test_job_form_fields(self):
        pass


class TimeEntryViewTests(TestCase):

    def test_time_entry_list_view_with_no_time_entrys(self):
        response = self.client.get(reverse('time_keeper:time_entry_index'))
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "<td>")
        self.assertQuerysetEqual(response.context['time_entrys'], [])

    def test_time_entry_list_view_with_time_entry_and_job(self):
        job = create_job()
        time_entry = create_time_entry(10, job, "test summary")
        response = self.client.get(reverse('time_keeper:time_entry_index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "test summary")
        self.assertQuerysetEqual(response.context['time_entrys'], 
            ["<TimeEntry: {}>".format(str(time_entry))])
   
    def test_time_entry_read_view(self):
        job = create_job()
        time_entry = create_time_entry(10, job, "test summary")
        response = self.client.get(reverse('time_keeper:time_entry_detail', 
            args=[time_entry.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "test summary")
    
    def test_time_entry_update_view_get(self):
        job = create_job()
        time_entry = create_time_entry(10, job, "test summary")
        response = self.client.get(reverse('time_keeper:time_entry_update', 
            args=[time_entry.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "test summary")
    
    def test_time_entry_delete_view_get(self):
        job = create_job()
        time_entry = create_time_entry(10, job, "test summary")
        response = self.client.get(reverse('time_keeper:time_entry_delete',
            args=[time_entry.id]), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "test summary")


class TimeEntryFormTests(TestCase):
    pass


class UtilTests(TestCase):
    
    def test_unit_string_singular(self):
        result = unit_string(1, "minute")
        self.assertEqual(result, "minute")

    def test_unit_string_plural(self):
        result = unit_string(2, "minute")
        self.assertEqual(result, "minutes")
