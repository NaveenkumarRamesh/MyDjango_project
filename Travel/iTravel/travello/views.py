from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return render(request,'home.html')    

def login(request):
    if request.method=='GET':
        return render(request,'login.html')

    elif request.method=='POST':
        user=request.POST['username']
        passw=request.POST['password']
        if user=='admin' and passw=='infy123':
            return render(request,'home.html',{'username':'admin'})
        return HttpResponse("Invalid user")

def view_profile(request):
    return HttpResponse("View")

def edit_profile(request):
    return HttpResponse("edit")


def delete_profile(request):
    return HttpResponse("delete")
