from django.urls import path,include
from travello import views

urlpatterns = [
    path("view/",views.view_profile),
    path("delete/",views.delete_profile),
    path("edit/",views.edit_profile),
    ]