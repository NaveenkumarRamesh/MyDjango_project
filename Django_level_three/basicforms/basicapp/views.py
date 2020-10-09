from django.shortcuts import render
from basicapp import forms 

# Create your views here.
def index(request):
    return render(request,"index.html",{"index_content":"enter forms/ to view form page"})

def formpage(request):
    form=forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("NAME:  "+form.cleaned_data['name'])
            print("EMAIL:  "+form.cleaned_data['email'])
            print("TEXT:  "+form.cleaned_data['text'])

    return render(request,"form.html",{"form":form})
