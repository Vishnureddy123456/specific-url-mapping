from django.urls import path
from app1.views import *
app_name='good'
urlpatterns=[
    path('msd/',msd,name='msd'),
    path('raina/',raina,name='raina'),
]