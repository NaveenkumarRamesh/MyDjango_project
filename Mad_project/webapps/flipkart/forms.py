from django import forms
from django.forms import ModelForm
from .models import Productname,Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        exclude = ()

class ProductnameForm(forms.ModelForm):
    class Meta:
        model = Productname
        fields = '__all__'