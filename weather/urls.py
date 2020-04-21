from django.urls import path
from . import views

urlpatterns = [
       path('', views.home, name = "home"),
       path('info', views.wethinf, name = "wethome"),
       path('lang', views.lang, name = "lang"),
       path('wetlang', views.wetlang, name = "wetlang"),
       path('langinfo', views.langinfo, name = "langinfo")
]
