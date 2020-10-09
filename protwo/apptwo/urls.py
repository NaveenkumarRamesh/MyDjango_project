from django.urls import path,re_path,include
from apptwo import views

urlpatterns = [
    # ex: /polls/5/vote/
    re_path(r'^$', views.call_database,name='db'),


]