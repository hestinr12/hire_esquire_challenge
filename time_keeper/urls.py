
from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.entry),
    url(r'^job/$', views.list_jobs),
    url(r'^time_entry/', views.list_time_entrys),
]
