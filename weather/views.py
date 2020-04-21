import requests
from django.shortcuts import render
from .models import weath

def home(request):
    return render(request, 'weather/home.html')

def wethinf(request):
     url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=86feeef11ba4a5d3bdfbe011b916a7a3&units=metric'
     city = request.POST['text']
     r = requests.get(url.format(city)).json()

     curr_weath={
        'city':city,
        'temperature':r['main']['temp'],
        'description':r['weather'][0]['description'],
        'icon':r['weather'][0]['icon']
        }
     return render(request, 'weather/weathinfo.html', {'curr_weath': curr_weath})

def lang(request):
    return render(request, 'weather/lang.html')

def wetlang(request):
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=86feeef11ba4a5d3bdfbe011b916a7a3&units=metric&lang={}'
        city = request.POST['text']
        lang = request.POST['lang']
        r = requests.get(url.format(city,lang)).json()
        curr_weath={
           'city':city,
           'temperature':r['main']['temp'],
           'description':r['weather'][0]['description'],
           'icon':r['weather'][0]['icon']
           }
        return render(request, 'weather/wetlang.html', {'curr_weath': curr_weath})

def langinfo(request):
    return render(request, 'weather/langinfo.html')
