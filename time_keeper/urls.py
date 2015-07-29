
from django.conf.urls import url

from . import views


urlpatterns = [
url(r'^$', views.entry),
    url(r'^job/$', views.list_jobs),
    url(r'^job/(?P<uuid>[0-9a-f\-]{36})/$', views.read_job),
    url(r'^job/(?P<uuid>[0-9a-f\-]{36})/create$', views.create_job),
    url(r'^job/(?P<uuid>[0-9a-f\-]{36})/update$', views.update_job),
    url(r'^job/(?P<uuid>[0-9a-f\-]{36})/delete$', views.delete_job),
    url(r'^time_entry/', views.list_time_entrys),
]
