import joblib as jb
import numpy as np

from prep_data import stock
from dataLoader import openPrice

model = jb.load(f"models/{stock}.pkl")

input = np.array(openPrice).reshape(-1, 1)

answer = model.predict(input)
 
answer = str(answer).replace("[", '')
answer = str(answer).replace("]", '')

percent = (float(answer) - openPrice)/openPrice


answer = round(float(answer), 2)
percent = round(float(percent), 2)


print(answer, percent)
