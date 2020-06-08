"""
PROBLEM 52
Write a program to print the output of the following poblem statement :-
You need to fetch the current conversion prices from the JSON using REST API?
"""
# get your api for free by registering on this website
import requests

url1 = "http://free.currencyconverterapi.com/api/v5/convert?q=USD_INR"
url2 = "&compact=ultra&apiKey=  "

url = url1 + url2

response = requests.get(url)
jsondata = response.json()

print ("Conversion rate of USD to INR", jsondata)

"""
conv = response.json()['USD_INR']*int(input(enter usd =>))
print(conv)
"""