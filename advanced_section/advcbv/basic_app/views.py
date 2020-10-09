from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView
from django.http import HttpResponse
from basic_app import models

# Create your views here.
class IndexView(TemplateView):
    template_name='index.html'

class SchoolListView(ListView):
    # context_object_name= 'schools'
    model = models.School

class SchoolDetailView(DetailView):
    context_object_name= 'schools_detail'
    model=models.School
