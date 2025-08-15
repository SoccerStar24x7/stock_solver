import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = pd.read_csv('data/COST_1YR copy.csv', usecols=["Open", "Close"])


# TRAINING:
# X: Open price
# y: Close price

