from django.conf.urls import url
from . import views           # This line is new!
  
urlpatterns = [

    url(r'^new$', views.new),  #you have to have $sign 
    url(r'^create$', views.create),
    url(r'^$', views.index),
    url(r'^(?P<number>\d+)$', views.show),
    url(r'^(?P<number>\d+)/edit$', views.edit),
    url(r'^(?P<number>\d+)/delete$', views.destroy)    # This line has changed!
    
    
]
