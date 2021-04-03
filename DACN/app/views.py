from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
#from dang nhap

# Create your views here.

def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request,'pages/index.html')


