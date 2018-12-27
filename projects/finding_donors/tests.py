# Import libraries necessary for this project
import numpy as np
import pandas as pd
from time import time
from IPython.display import display # Allows the use of display() for DataFrames

# Load the Census dataset
data = pd.read_csv("census.csv")

print(data.head())

print(len(data))

a = data['income'] != '>=50K'
print(len(data[a]))