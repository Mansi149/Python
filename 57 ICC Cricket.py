"""
PROBLEM 57
Write a program to print the output of the following poblem statement :-
Scrap the data from the URL below and store in mySQL database
https://www.icc-cricket.com/rankings/mens/team-rankings/odi ?
"""

from bs4 import BeautifulSoup
import requests
import mysql.connector

x = requests.get("https://www.icc-cricket.com/rankings/mens/team-rankings/odi").text
soup = BeautifulSoup(x,"lxml")

t = soup.find('table', class_='table')

Team = []
Matches = []
Points = []
Rating = []

for row in t.findAll('tr') :
    cells = row.findAll('td')
    if len(cells) == 5 :
        Team.append(cells[1].text.strip()[:-4:])
        Matches.append(cells[2].text.strip())
        Points.append(cells[3].text.strip())
        Rating.append(cells[4].text.strip())
        
print(Team, Matches, Points, Rating)

con = mysql.connector.connect(user = ' ', password = ' ', host = 'db4free.net', database = ' ')
bridge = con.cursor()
bridge.execute("""CREATE TABLE rank(
            Team TEXT,
            Matches TEXT,
            Points TEXT,
            Rating TEXT
            )
         """)
con.commit()

sql = "INSERT INTO rank (Teams, Matches, Points, Rating) VALUES (%s, %s, %s, %s)"
value = []
for i in range(len(Team)) :
    s = (Team[i], Matches[i], Points[i], Rating[i]) 
    value.append(s)

bridge.executemany(sql, value)
con.commit()

bridge.execute("SELECT * FROM rank")
from pandas import DataFrame
df = DataFrame(bridge.fetchall())  
df.columns = ["TEAM NAME", "MATCHES", "POINTS", "RATING"]
print(df)

con.close()

