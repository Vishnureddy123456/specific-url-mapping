from django.urls import path
from app2.views import *
app_name='bad'
urlpatterns=[
    path('virat/',virat,name='virat')
]