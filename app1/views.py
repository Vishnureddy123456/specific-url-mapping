from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def msd(request):
    return HttpResponse('<h1>MSD IS THE BEST CAPTAIN</h1>')
def raina(request):
    return HttpResponse('<h1>RAINA IS MR IPL</h1>')
