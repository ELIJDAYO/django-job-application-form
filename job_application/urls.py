from django.urls import path
from . import views

urlpatterns = [
    # params: direc in url, get fun index, ...
    path('', views.index, name="index")
]