from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
#from dang nhap

# Create your views here.

def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request,'pages/index.html')

def _about(request):
    return render(request,'pages/about.html')

def _chandoan(request):
    return render(request,'pages/chandoan.html')

def _lienhe(request):
    return render(request,'pages/contact.html')


