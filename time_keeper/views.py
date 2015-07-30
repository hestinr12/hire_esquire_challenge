from django.shortcuts import get_list_or_404, get_object_or_404, \
    redirect, render
from django.core.urlresolvers import reverse 
from django.http import HttpResponseBadRequest

from .models import Job, TimeEntry
from .forms import JobForm, TimeEntryForm

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

def create_job(request):
    '''
    GET: Send form 
    POST: Process form'''

    if request.method == "GET":
        form = JobForm()
    elif request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save()
            return redirect(reverse('time_keeper:job_detail', args=(job.id,)))
    
    return render(request, 'time_keeper/form.html', {
        'message': 'New Job',
        'forward_address': 'time_keeper:job_create',
        'form': form,
    })

def update_job(request, uuid):
    '''
    GET: Send form from model
    POST: Update model from form'''
    
    job = Job.objects.get(pk=uuid)
    
    if request.method == "GET":
        form = JobForm(instance=job)
    elif request.method == "POST":
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            job = form.save()
            return redirect(reverse('time_keeper:job_detail', args=(job.id,)))

    return render(request, 'time_keeper/form.html', {
        'message': 'Update Job',
        'forward_address': 'time_keeper:job_update',
        'url_arg': uuid,
        'form': form,
    })

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
