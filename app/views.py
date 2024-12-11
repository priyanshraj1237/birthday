from django.shortcuts import render,HttpResponse

def home(request):
    return HttpResponse(" u are in home page of app")

def wish(request):
    return render (request,"app/index.html")
