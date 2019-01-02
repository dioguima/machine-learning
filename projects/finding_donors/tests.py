# Import libraries necessary for this project
import numpy as np
import pandas as pd
from time import time
from IPython.display import display # Allows the use of display() for DataFrames

from sklearn.model_selection.cross_validate import train_test_split

# Load the Census dataset
data = pd.read_csv("census.csv")

print(data.head())

print(len(data))

a = data['income'] != '>=50K'
print(len(data[a]))

income = pd.get_dummies(data['income'])
