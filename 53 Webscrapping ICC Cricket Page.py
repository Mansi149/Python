"""
PROBLEM 53
Write a Python code to Scrap data from ICC Ranking's 
page and get the ranking table for ODI's (Men). 
Create a DataFrame using pandas to store the information.
Hint : https://www.icc-cricket.com/rankings/mens/team-rankings/odi ?
"""

from bs4 import BeautifulSoup
import requests
icc = "https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
source = requests.get(icc).text
soup = BeautifulSoup(source,"lxml")
new_table = soup.find('table', class_='table')

print (new_table)

A = []
B = []
C = []
D = []
E = []

for body in new_table.findAll('tbody'):
    for row in body.find_all('tr'):
        cells = row.findAll('td')
        A.append(cells[0].text.strip())
        B.append(cells[1].text.strip())
        C.append(cells[2].text.strip())
        D.append(cells[3].text.strip())
        E.append(cells[4].text.strip())
import pandas
data_frame = pandas.DataFrame()
data_frame["position"] = A 
data_frame["team"] = B 
data_frame["matches"] = C 
data_frame["points"] = D 
data_frame["rating"] = E  
data_frame.to_csv("ODI_Ranking_2017.csv", index = False) 