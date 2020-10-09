from django.shortcuts import render
from .forms import FeedbackForm
from django.http import HttpResponse
from .models import Productname

def feedback(request):
    if request.method == 'GET':
        form = FeedbackForm
        return render(request,'feedback.html',{
            'form': form,
        })

    elif request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Saved!")
# Create your views here.
def home(request):
    content = Productname.objects.all
    # category = Productname.objects.values('category')
    return render(request,'home.html',{'content':content})

def moreinfo(request):
    user_category=request.GET.get('category')
    content=Productname.objects.filter(category=user_category).values_list('id','productname','price')
    return render(request,'moreinfo.html',{'content':content})

def explore(request):
    id = request.GET.get('product_id')
    content=Productname.objects.filter(id=id).values()
    content= content[0]
    return render(request,'explore.html',{'content':content})