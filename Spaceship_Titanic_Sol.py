# .py file that uses machine learning methods to determine whether or not
# passengers on the Spaceship Titanic were teleoported to another dimension

# Export train data into python from csv file
import pandas as pd
train = pd.read_csv("/Users/drakeshaub/Documents/GitHub Desktop/Kaggle - Spaceship Titanic/Kaggle_Spaceship_Titanic/train.csv")
# check to see if import worked
train.head()

