from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login(request):
    return HttpResponse("Login View")

def signup(request):
    return HttpResponse("Signup View")