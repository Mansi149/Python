"""
PROBLEM 62
Write a program to print the output of the following poblem statement :-
It’s a real-world data containing the details of 
      titanic ships passengers list.
      Import the training set "training_titanic.csv"
      
      PassengerId
      survival: Survival (0 = No; 1 = Yes)
      pclass: Passenger Class (1 = Upper; 2 = Middle; 3 = Lower)
      name: Name
      sex: Sex
      age: Age 
      sibsp: Number of Siblings/Spouses Aboard
      parch: Number of Parents/Children Aboard
      ticket: Ticket Number
      fare: Passenger Fare
      cabin: Cabin
      embarked: Port of Embarkation 
      (C = Cherbourg; Q = Queenstown; S = Southampton)
      
  Answer the Following:
      How many people survived the disaster ?
      
      How many people died ?
      
      Calculate the survival rates as proportions (percentage)
      
      Males that survived vs males that passed away
      
      Females that survived vs Females that passed away      
      
      Does age play a role?
      Since it's probable that children were saved first?
"""

import pandas as pd
df = pd.read_csv("training_titanic.csv")

x = df.Survived.value_counts()

# How many people died ?
dead = x.values[0]
print("People who died :", dead )

# How many people survived the disaster ?
alive = x.values[1]
print("People who survived :", alive )

# Calculate the survival rates as proportions (percentage)
print("Survival Rate :", alive / (alive + dead) *100)

# Males that survived vs males that passed away
alive_male = len( df[(df.Sex == 'male') & (df.Survived == 1)] ) 
dead_male = len( df[(df.Sex == 'male') & (df.Survived == 0)] )
print("Survial rate of males :", alive_male / (alive_male + dead_male) * 100)

# Females that survived vs Females that passed away      
alive_female = len( df[(df.Sex == 'female') & (df.Survived == 1)] ) 
dead_female = len( df[(df.Sex == 'female') & (df.Survived == 0)] )
print("Survial rate of females :", alive_male / (alive_female + dead_female) * 100)

# Does age play a role? Since it's probable that children were saved first.
x = df.Survived.value_counts()
alive = x.values[1]

df1 =  df[df.Survived==1][df.Age <= 18]
print("Child survival rate :", len(df1['Age']) * 100 / alive)

