from . import views
from django.conf.urls import url
from django.urls import path

app_name = 'offenses'
urlpatterns = [
    # path('', views.index, name='offenses'),
    url(r'^$',views.index, name='offenses'),
    ]