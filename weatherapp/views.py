from django.shortcuts import render
from django.http import HttpResponse
import requests
import datetime

# Create your views here.

def home(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'bhubaneswar'
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=2976289e4452380072b1ab55f9054c86"

    params = {"units":"metric"}
    data = requests.get(url,params=params).json()
    description = data['weather'][0]['description']
    icon = data['weather'][0]['icon']
    temp = data['main']['temp']

    day = datetime.date.today()
    return render(request,'index.html',
    {'description':description,'icon':icon,'temp':temp,'day':day,'city':city})