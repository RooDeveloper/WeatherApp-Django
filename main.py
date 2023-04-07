import datetime
import requests
from datetime import datetime  
import pytz  
from timezonefinder import TimezoneFinder
from queue import Queue
from urllib.request import urlopen
import json
currentCity = "to kyo"

#weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={currentCity}&units=imperial&APPID=81aa3bb8ea9237f662cdf4e053692252")
#weather = weather_data.json()['weather'][0]['main']
#tempF = weather_data.json()['main']['temp']
#tempC = round((tempF-32)/1.8)
#city = weather_data.json()['name']
#wind = weather_data.json()['wind']['speed']
#humidity = weather_data.json()['main']['humidity']
#clouds = weather_data.json()['clouds']['all']


class Queue:

    def __init__(self):
        self.queue = []

    # Add an element
    def enqueue(self, item):
        self.queue.append(item)

    # Remove an element
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    # Display  the queue
    def display(self):
        print(self.queue)

    def size(self):
        return len(self.queue)


ipinfo = requests.get('http://ipinfo.io/json')
#response = urlopen(url)
#data = str(json.loads(response))
print(ipinfo.json()['ip'])

import socket
## getting the hostname by socket.gethostname() method
hostname = socket.gethostname()
## getting the IP address using socket.gethostbyname() method
ip_address = socket.gethostbyname(hostname)
## printing the hostname and ip_address
#print(f"Hostname: {hostname}")
#print(f"IP Address: {ip_address}")
if request.is_ajax and request.method == "GET" :
            if  request.method == "GET":
                currentcity = get_location(request.GET.get('IPval',""))["city"]
                #print("----",request.GET.get('IPval',""))
                data = cityLists.getCityList()
                data.reverse()
                weatherinfo = weatherdata(currentcity)
                bg = backgroundImage(weatherinfo.type)
                return render(request,"home.html",{'weatherInfo': weatherinfo,'bgname':bg,'data':data})

def get_location(ip):
    #ipinfo = requests.get('http://ipinfo.io/json')
    #ip_address = ipinfo.json()['ip']
    response = requests.get(f'https://api.ipgeolocation.io/ipgeo?apiKey=29dcc74f74b44cdcbc2e49d04e90cb8e&ip={ip}').json()
    location_data = {
        "ip": ip_address,
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name")
    }
    return location_data


print(get_location("2402:4000:20c3:4fc3:bdca:c5e:16cc:325")["city"])