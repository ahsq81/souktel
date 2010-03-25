# To change this template, choose Tools | Templates
# and open the template in the editor.

from django.conf.urls.defaults import *
import views

urlpatterns = patterns('',
    url(r'^survey/?$', views.index),
    url(r'^survey/(\d+)/?$', views.profile, name="profile")
)