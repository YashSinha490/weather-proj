from django.urls import path
from . import views

urlpatterns = [
       path('', views.wethinf, name = "wethome"),
]
