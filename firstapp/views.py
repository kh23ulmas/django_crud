from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello world Azisasza")

def about(request):
    return HttpResponse("<h2>About Us</h2>")

def contacts(request):
    return HttpResponse("<h2>Contacts</h2>")


