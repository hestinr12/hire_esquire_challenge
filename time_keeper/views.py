from django.shortcuts import get_list_or_404, get_object_or_404, \
    redirect, render
from django.core.urlresolvers import reverse 
from django.http import HttpResponseBadRequest

from .models import Job, TimeEntry

# Create your views here.

def entry(request):
    return render(request, 'time_keeper/index.html', {
            'objects': [
                '/admin',
                '/job'
                '/job/...',
                '/time_entry'
                '/time_entry/...'
            ]
        })

def list_jobs(request):
    jobs = Job.objects.all()
    return render(request, 'time_keeper/job_index.html', {'jobs': jobs})

def read_job(request, uuid):
    job = get_object_or_404(Job, id=uuid)
    return render(request, 'time_keeper/job_detail.html', {'job': job})

def new_job(request):
    '''render form for Job'''
    pass

def create_job(request):
    '''add Job and redirect success/fail'''
    pass

def update_job(request, uuid):
    pass

def delete_job(request, uuid):
    if request.method == "GET":
        job = get_object_or_404(Job, id=uuid)
        message = ''
        try:
            job.delete()
            message = 'Delete successful.'
        except:
            message = 'Object exists, but deletion failed.'
    else:
        return HttpResponseBadRequest('SWAP GET FOR POST IN delete_job') # todo
    return redirect(reverse('time_keeper:job_index'))

def list_time_entrys(request):
    time_entries = TimeEntry.objects.all()
    return render(request, 'time_keeper/index.html', {'objects': time_entries})
