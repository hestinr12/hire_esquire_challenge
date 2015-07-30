
from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.entry, name='entry'),
    url(r'^job/$', views.list_jobs, name='job_index'),
    url(r'^job/(?P<uuid>[0-9a-f\-]{36})/$', views.read_job, name='job_detail'),
    url(r'^job/create$', views.create_job, name='job_create'),
    url(r'^job/(?P<uuid>[0-9a-f\-]{36})/update$', views.update_job,
        name='job_update'),
    url(r'^job/(?P<uuid>[0-9a-f\-]{36})/delete$', views.delete_job,
        name='job_delete'),
    url(r'^time_entry/$', views.list_time_entrys, name='time_entry_index'),
    url(r'^time_entry/(?P<pk>[0-9])/$', views.read_time_entry,
        name='time_entry_detail'),
    url(r'^time_entry/create$', views.create_time_entry,
        name='time_entry_create'),
    url(r'^time_entry/(?P<pk>[0-9])/update$', views.update_time_entry,
        name='time_entry_update'),
    url(r'^time_entry/(?P<pk>[0-9])/delete$', views.delete_time_entry,
        name='time_entry_delete'),
]
