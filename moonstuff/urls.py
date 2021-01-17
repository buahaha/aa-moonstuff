from django.conf.urls import url

from . import views

app_name = "moonstuff"

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^scan/$', views.add_scan, name='add_scan'),
    url(r'^track/$', views.add_character, name='add_character'),
]
