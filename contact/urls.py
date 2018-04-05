from django.conf.urls import url
from . import views

app_name="contact"

urlpatterns = [
    url(r'^$', views.view, name='index'),
    url(r'^create/$', views.create , name='create'),
    url(r'^create-post/$', views.create_post, name='create-post'),
    url(r'^update/(?P<contactId>[0-9]+)/$', views.update, name='update'),
    url(r'^update-post/(?P<contactId>[0-9]+)/$', views.update_post, name='update-post'),
    url(r'^delete-post/(?P<contactId>[0-9]+)/$', views.delete_post, name='delete-post'),
]
