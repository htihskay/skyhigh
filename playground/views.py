from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def calculate():
    x=1
    y=3
    z=7
    return(x+y+z)

def sayHello(request):
    x=1
    x=2
    x=calculate()
    return render(request,"yaxith.html",{"name":"yakshith"})
    #return HttpResponse("hello this is Yakshith")