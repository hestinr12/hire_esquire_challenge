from django.shortcuts import get_list_or_404, get_object_or_404, \
    redirect, render
from django.core.urlresolvers import reverse 
from django.http import HttpResponseBadRequest

from .models import Job, TimeEntry
from .forms import JobForm, TimeEntryForm

# Create your views here.

def entry(request):
    return render(request, 'time_keeper/index.html')

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
    time_entrys = TimeEntry.objects.all()
    return render(request, 'time_keeper/time_entry_index.html', {
        'time_entrys': time_entrys,
    })

def read_time_entry(request, pk):
    time_entry = get_object_or_404(TimeEntry, pk=pk)
    return render(request, 'time_keeper/time_entry_detail.html', {'time_entry': time_entry})

def create_time_entry(request):
    '''
    GET: Send form 
    POST: Process form'''

    if request.method == "GET":
        form = TimeEntryForm()
    elif request.method == "POST":
        form = TimeEntryForm(request.POST)
        if form.is_valid():
            time_entry = form.save()
            time_entry.related_job.updateTotalMinutes()
            return redirect(reverse('time_keeper:time_entry_detail', args=(time_entry.pk,)))
    
    return render(request, 'time_keeper/form.html', {
        'message': 'New Time Entry',
        'forward_address': 'time_keeper:time_entry_create',
        'form': form,
    })

def update_time_entry(request, pk):
    '''
    GET: Send form from model
    POST: Update model from form'''
    
    time_entry = TimeEntry.objects.get(pk=pk)
    
    if request.method == "GET":
        form = TimeEntryForm(instance=time_entry)
    elif request.method == "POST":
        form = TimeEntryForm(request.POST, instance=time_entry)
        if form.is_valid():
            time_entry = form.save()
            time_entry.related_job.updateTotalMinutes()
            return redirect(reverse('time_keeper:time_entry_detail', args=(time_entry.pk,)))

    return render(request, 'time_keeper/form.html', {
        'message': 'Update Time Entry',
        'forward_address': 'time_keeper:time_entry_update',
        'url_arg': pk,
        'form': form,
    })

def delete_time_entry(request, pk):
    if request.method == "GET":
        time_entry = get_object_or_404(TimeEntry, pk=pk)
        message = ''
        try:
            time_entry.delete()
            message = 'Delete successful.'
        except:
            message = 'Object exists, but deletion failed.'
    else:
        return HttpResponseBadRequest('SWAP GET FOR POST IN delete_time_entry') # todo
    return redirect(reverse('time_keeper:time_entry_index'))
