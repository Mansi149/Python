"""
PROBLEM 61
Write a program to print the output of the following poblem statement :-
Perform the following task :
1. Handle the missing values for Price column
2. Get the values from Price column into a numpy.ndarray
3. Calculate the Minimum Price, Maximum Price, Average Price and Standard Deviation of Price
4. Make a pie chart for all car makers
"""

import numpy
import pandas as pd
import matplotlib.pyplot as plot
df = pd.read_csv("Automobile.csv")

# Handle the missing values for Price column
x = df [ df [ 'price' ].isnull() ]
print(x.fillna(0))

# Get the values from Price column into a numpy.ndarray
y = numpy.array( df.price.tolist() )
type(y)

# Calculate the Minimum Price, Maximum Price, Average Price and Standard Deviation of Price
print("Average price is:", df.price.mean() )
print("Minimum price is:", df.price.min() )
print("Maximum price is:", df.price.max() )
print("Standard deviation of price is:", df.price.std() )

# Make a pie chart for all car makers
count = dict(df['make'].value_counts())
plot.title('Car Brands')
plot.pie(count.values(),
         labels = count.keys(),
         
         shadow = True,
         autopct = '%.1f%%'
         )
plot.axis('equal')