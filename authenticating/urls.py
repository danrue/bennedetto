from django.conf.urls import include, url

from authenticating import views

urlpatterns = [
    url(r'^register/$', views.Register.as_view(), name='register'),
    url(r'^', include('django.contrib.auth.urls')),
]
