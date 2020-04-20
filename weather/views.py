import requests
from django.shortcuts import render
from .models import weath

def wethinf(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=86feeef11ba4a5d3bdfbe011b916a7a3&units=metric'


    allweath = []
    for city in weath.objects.all():
        r = requests.get(url.format(city)).json()

        curr_weath={
            'city':city,
            'temperature':r['main']['temp'],
            'description':r['weather'][0]['description'],
            'icon':r['weather'][0]['icon']
        }
        allweath.append(curr_weath)


    print(allweath)
    return render(request, 'weather/home.html', {'allweath':allweath} )
