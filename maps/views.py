from django.shortcuts import render
import requests
def audio(request):
    data = request.POST.get('record')
    import speech_recognition as sr

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak:")
        audio = r.listen(source)

    try:
        output = " " + r.recognize_google(audio)
    except sr.UnknownValueError:
        output = "Could not understand audio"
    except sr.RequestError as e:
        output = "Could not request results; {}".format(e)
    data = output

    try:
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=86feeef11ba4a5d3bdfbe011b916a7a3&units=metric'
        r = requests.get(url.format(data)).json()
        curr_weath={
          'city':r['name'],
          'temperature':r['main']['temp'],
          'description':r['weather'][0]['description'],
          'icon':r['weather'][0]['icon']
          }
        return render(request, 'maps/main.html', {'curr_weath': curr_weath})
    except KeyError:
        return render(request, 'maps/wrngke.html',{'say': data})
