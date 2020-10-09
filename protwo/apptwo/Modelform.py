from django import forms
from apptwo.models import user
from django.core import validators


def checkField(values):
    if values.length() < 1:
        raise Validation.Error("Enter email name")
class MyNewForm(forms.ModelForm):
    class Meta:
        model = user
        fields = "__all__"