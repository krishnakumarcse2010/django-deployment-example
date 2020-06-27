from django.urls import path
from . import views

app_name = 'basicapp'
urlpatterns = [
    path('register',views.register,name='basic'),
    path('',views.index,name='index'),
]
