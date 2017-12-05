from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'ister/$', views.register),
    url(r'in/$', views.login),
    url(r'^new/$', views.register),
    url(r'^$', views.users),
]