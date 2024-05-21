from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello, world. You're at the Django Home")
    return render(request, 'website/index.html')

def about(request):
    return HttpResponse("You're at the about ")

def contact(request):
    return HttpResponse("You're at the contact")


