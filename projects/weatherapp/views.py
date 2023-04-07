from django.shortcuts import render
from django.http import HttpResponse
import requests
from . models import wetherInfoData, SearchList
from datetime import datetime  
import pytz  
from timezonefinder import TimezoneFinder
import random
import json

cityLists = SearchList()
# Create your views here.
def weatherdata(city):
    weatherInfo = wetherInfoData()
    currentCity = city
    weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={currentCity}&units=imperial&APPID=81aa3bb8ea9237f662cdf4e053692252")
    if weather_data.json()['cod'] != '404':
        weatherInfo.type = weather_data.json()['weather'][0]['main']
        weatherInfo.icon = weather_data.json()['weather'][0]['icon']
        weatherDescription = weather_data.json()['weather'][0]['description']
        weatherInfo.weather = weatherDescription.title()
        tempF = weather_data.json()['main']['temp']
        weatherInfo.temp = round((tempF-32)/1.8)

        weatherInfo.city = weather_data.json()['name']
        weatherInfo.wind = weather_data.json()['wind']['speed']
        weatherInfo.humidity = weather_data.json()['main']['humidity']
        weatherInfo.clouds = weather_data.json()['clouds']['all']
        weatherInfo.status = "200"

        #getTime
        tf = TimezoneFinder()
        lonn = weather_data.json()['coord']['lon']
        latt = weather_data.json()['coord']['lat']

        tz = tf.timezone_at(lng=lonn, lat=latt)

        cityTimezone = pytz.timezone(tz) 
        timeInCity = datetime.now(cityTimezone)
        weatherInfo.datetime = timeInCity.strftime("%H:%M %A %B %d %Y")
    else:
        weatherInfo.type  = "not found"
        weatherInfo.icon  = "not found"
        weatherInfo.city  = "not found"
        weatherInfo.weather = "not found"
        weatherInfo.temp = "00"
        weatherInfo.wind = "not found"
        weatherInfo.humidity = "not found"
        weatherInfo.clouds = "not found"
        weatherInfo.datetime  = "not found"
        weatherInfo.status = "404"

    return weatherInfo

def backgroundImage(weather):
    sunny = ["https://i.postimg.cc/g2gRZzNj/pexels-johannes-plenio-1632781.jpg","https://i.postimg.cc/PJHN7920/pexels-damon-hall-1647177.jpg"]
    cloudy = ["https://i.postimg.cc/SxCLd4pF/pexels-pixabay-45848.jpg","https://i.postimg.cc/rFWgnxSP/pexels-donald-tong-55787.jpg","https://i.postimg.cc/g0MKXDWn/pexels-nur-andi-ravsanjani-gusma-1465904.jpg"]
    windy = ["https://i.postimg.cc/8z7pCZ69/pexels-eberhard-grossgasteiger-1074428.jpg"]
    rainy = ["https://i.postimg.cc/gJZ4kbzj/pexels-kaique-rocha-125510.jpg","https://i.postimg.cc/zXXWxYsh/pexels-pixabay-531906.jpg","https://i.postimg.cc/Vv7Jx5xC/pexels-pixabay-373481.jpg"]
    stromy = ["https://i.postimg.cc/8z7pCZ69/pexels-eberhard-grossgasteiger-1074428.jpg"]
    mist = ["https://i.postimg.cc/wMBY3kv7/pexels-karol-wi-niewski-845619.jpg"]
    if weather == "Clear":
        return random.choice(sunny)
    elif weather == "Clouds":
        return random.choice(cloudy)
    elif weather == "Smoke":
        return random.choice(windy)
    elif weather == "Rain":
        return random.choice(rainy)
    elif weather == "Thunderstorm":
        return random.choice(stromy)
    elif weather == "Mist":
        return random.choice(mist)
    else:
        return "https://i.postimg.cc/wMBY3kv7/pexels-karol-wi-niewski-845619.jpg"


def get_location(ip_address):
    #ipinfo = requests.get('http://ipinfo.io/json')
    #ip_address = ipinfo.json()['ip']
    response = requests.get(f'https://api.ipgeolocation.io/ipgeo?apiKey=29dcc74f74b44cdcbc2e49d04e90cb8e&ip={ip_address}').json()
    location_data = {
        "ip": ip_address,
        "city": response.get("country_capital"),
        "region": response.get("region"),
        "country": response.get("country_name")
    }
    return location_data

def home(request):
    
    #data.reverse()
    if request.method=="POST" :
        if request.POST.get('city'):
            weatherinfo = weatherdata(request.POST.get('city'))
            if weatherinfo.status == "200":
                cityLists.add(request.POST.get('city'))
            data = cityLists.getCityList()
            data.reverse()

            bg = backgroundImage(weatherinfo.type)
            return render(request,"home.html",{'weatherInfo': weatherinfo,'bgname':bg,'data':data})
    else:
                ipinfo = requests.get('http://ipinfo.io/json')
                ip_address = ipinfo.json()['ip']
                currentcity = get_location(ip_address)["city"]
                #print("----",request.GET.get('IPval',""))
                data = cityLists.getCityList()
                data.reverse()
                weatherinfo = weatherdata(currentcity)
                bg = backgroundImage(weatherinfo.type)
                return render(request,"home.html",{'weatherInfo': weatherinfo,'bgname':bg,'data':data})
            
            

