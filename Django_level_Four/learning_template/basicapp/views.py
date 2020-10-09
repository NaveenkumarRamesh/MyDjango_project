from django.shortcuts import render

# Create your views here.
def mainPage(request):
    context_dict={"name":"hello world","number":100}
    return render(request,'base_app/index.html',context_dict)

def relativePage(request):
    return render(request,'base_app/relative_url.html')

def otherPage(request):
    return render(request,'base_app/other.html')

