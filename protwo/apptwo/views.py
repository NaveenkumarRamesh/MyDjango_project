from django.shortcuts import render
from django.http import HttpResponse
from apptwo.models import user
from apptwo.Modelform import MyNewForm


# Create your views here.
def display(name):
    return HttpResponse("<h1>this is second project</h1>")


# def call_database(request):
#     user_list = user.objects.order_by("FirstName")
#     db_dict={"userdb":user_list}
#     return render(request,"user.html",context=db_dict)
def call_database(request):
    form=MyNewForm()
    if request.method == "POST":
        form = MyNewForm(request.POST)
        if form.is_valid:
            form.save(commit=True)
            return call_Html(request)
        else:
            print("error")
    return render(request,"user.html",{"form":form})

def call_Html(request):
    html_dict={"index":"Welcome to django"}
    return render(request,"help.html",context=html_dict)