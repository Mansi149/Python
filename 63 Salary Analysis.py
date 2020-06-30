"""
PROBLEM 63
Write a program to print the output of the following poblem statement :-
Analysis of Salaries Data

1. Which Male Professor has the highest and the lowest salaries

1. Which Female Professor has the highest and the lowest salaries
   
2. Which Professor takes the highest and lowest salaries.

3. Missing Salaries - should be mean of the matching salaries of those 
   whose service is the same
   
4. Missing phd - should be mean of the matching service 

5. How many are Male Staff and how many are Female Staff. 
   Show both numbers and in percentage
   Show both in numbers and Graphically using Pie Chart.  
   
6. How many are Prof, AssocProf and AsstProf. 
   Show both in numbers and Graphically using a Pie Chart   

7. Who are the senior and junior most employees in the organization.

8. Draw a histogram of the salaries divided into bin starting 
   from 50K and increment of 15K ?
"""

import pandas as pd
import matplotlib.pyplot as plot



df = pd.read_csv("Salaries.csv")

# Which Male Professor has the highest and the lowest salaries
filter = df[ df.sex == 'Male']
print("Details of professor with minimum salary :\n", filter.min())
print("Details of professor with maximum salary :\n", filter.max())

# Which Female Professor has the highest and the lowest salaries
filter = df[ df.sex == 'Female']
print("Details of professor with minimum salary :\n", filter.min())
print("Details of professor with maximum salary :\n", filter.max())
  
# Which Professor takes the highest and lowest salaries.
print("Details of professor with highest salary :", df[['rank','discipline','phd','service','sex','salary']].max())
print("Details of professor with lowest salary :", df[['rank','discipline','phd','service','sex','salary']].min())

# How many are Male Staff and how many are Female Staff Show both numbers and in percentage 
Series1 = df.sex.value_counts() 
male = Series1['Male']
female = Series1['Female']    
print("Male professors :", male, "\nFemale professors :", female)
print("Percentage of male staff :", male / (male + female) * 100)     
print("Percentage of female staff :", female / (male + female) * 100) 

# How many are Prof, AssocProf and AsstProf. Show both in numbers and Graphically using a Pie Chart   
Series2 = df['rank'].value_counts()
professor = Series2['Prof']
Assistant_professor = Series2['AsstProf']
Associate_professor = Series2['AssocProf']
print("Professor count :", professor, "\nAssistant professor count :", Assistant_professor, "\nAssociate professor count :", Associate_professor)

# Who are the senior and junior most employees in the organization.
print("The seniormost employee is : \n",df[(df['service']==df['service'].max())])
print("The juniormost employee is : \n",df[(df['service']==df['service'].min())])

# Draw a histogram of the salaries divided into bin starting from 50K and increment of 15K
hist11 = list(df['salary'])
hist11.sort()
plot.xlabel('salary')
plot.ylabel('prof,asscprof,assocprof')
plot.hist(hist11,bins = [50000,65000,80000,95000,110000,125000,140000,155000,170000,185000,200000])






