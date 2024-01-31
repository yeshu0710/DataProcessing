#importing libaries
import numpy as npy
import matplotlib.pyplot as plt
import pandas as pd

#importing dataset
dataset = pd.read_csv("Data.csv")
independent_var = dataset.iloc[:,:-1].values
dependent_var = dataset.iloc[:,-1].values
print(independent_var)
print(dependent_var)
#print(type(independent_var))
#print(type(dependent_var))

