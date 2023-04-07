from django.db import models

# Create your models here.
class wetherInfoData:
    type : str
    icon : str
    city : str
    weather :str
    temp :str
    wind :str
    humidity :str
    clouds :str
    datetime : str
    status : str

class SearchList:
    def __init__(self):
        self.__cityList = ["New York", "Paris", "Tokyo", "Califonia","London"]

    def getCityList(self):
        data = self.__cityList[-5::]
        return data

    def add(self, city):
        if city in self.__cityList:
            self.__cityList.remove(city)
            self.__cityList.append(city.capitalize())
        else:
            self.__cityList.append(city.capitalize())
            self.__cityList.pop(0)