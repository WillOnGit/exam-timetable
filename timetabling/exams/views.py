from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def index(request):
    return(HttpResponse("Hiya! You're logged in as %s."%request.user))
