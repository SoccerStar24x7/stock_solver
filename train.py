import numpy as np
import joblib as jb
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

from prep_data import data
from dataLoader import stock


# TRAINING:
# X: Open price
# y: Close price

X = np.array(data["Open"]).reshape(-1, 1)
y = np.array(data["Close"]).reshape(-1, 1)

# Splitting the data into training and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

model = LinearRegression()

model.fit(X_train, y_train)

print(model.score(X_test, y_test))

# save model

jb.dump(model, f"models/{stock}.pkl") 
