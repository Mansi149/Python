"""
PROBLEM 51
Write a program to print the output of the following poblem statement :-
Get me the other details about the city
        Latitude and Longitude
        Weather Condition
        Wind Speed
        Sunset Rise and Set timing?
"""
# get your api for free by registering on this website
import requests

city = input("Weather information of the city needed: ")

url1 = "http://api.openweathermap.org/data/2.5/weather"
url2 = "?q=" + city
url3 = "&appid=  "

url = url1 + url2 + url3

response = requests.get(url)
jsondata = response.json()

print ("Climate Conditions for the city of", city, "->")
print ("Temperature :", jsondata['main']['temp']- 273.15, "degree Celsius")
print("Weather condition :",jsondata['weather'][0]['description'])
print ("Latitude :", jsondata['coord']['lat'])
print ("Longitude :", jsondata['coord']['lon'])
print ("Wind Speed :", jsondata['wind']['speed'])

import time

print("Sunrise Time :", time.ctime(jsondata['sys']['sunrise']))
print("Sunset Time :", time.ctime(jsondata['sys']['sunset']))