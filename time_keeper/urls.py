
from django.conf.urls import url

from . import views


urlpatterns = [
url(r'^$', views.entry),
    url(r'^job/$', views.list_jobs, name='job_index'),
    url(r'^job/(?P<uuid>[0-9a-f\-]{36})/$', views.read_job, name='job_detail'),
    url(r'^job/new$', views.new_job, name='job_new'),
    url(r'^job/create$', views.create_job, name='job_create'),
    url(r'^job/(?P<uuid>[0-9a-f\-]{36})/update$', views.update_job,
        name='job_update'),
    url(r'^job/(?P<uuid>[0-9a-f\-]{36})/delete$', views.delete_job,
        name='job_delete'),
    url(r'^time_entry/', views.list_time_entrys),
]
