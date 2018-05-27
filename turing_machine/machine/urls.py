from django.conf.urls import url, include
from django.urls import path
from . import views
app_name = 'machine'

urlpatterns = [
    path('', views.index, name='index'),
    path('machine', views.t_m, name='t_m'),
]
