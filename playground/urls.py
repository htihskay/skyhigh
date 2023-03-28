from django.urls import path
from . import views

urlpatterns = [
    path("yaxith/",views.sayHello)
]