from django.urls import path
from . import views

urlpatterns = [
       path('', views.home, name = "home"),
       path('info', views.wethinf, name = "wethome")
]
