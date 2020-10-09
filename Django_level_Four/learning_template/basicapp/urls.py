from django.urls import path,re_path
from basicapp import views

app_name = 'basicapp'

urlpatterns = [
    re_path(r'^relative/$',views.relativePage,name='relativepage'),
    re_path(r'^other/$',views.otherPage,name='otherPage'),
]

