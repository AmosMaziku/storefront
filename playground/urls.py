from django.urls import path
from . import views


urlpatterns = [
    path('', views.empty_parameter),
    path('hello', views.say_hello),
]