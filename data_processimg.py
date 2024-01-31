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

#Removing Missing values
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=npy.nan, strategy='mean')
imputer.fit(independent_var[:, 1:3])
independent_var[:, 1:3] = imputer.transform(independent_var[:, 1:3])
print(independent_var)