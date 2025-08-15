import pandas as pd

from dataLoader import stock

# Read the CSV, specifying the columns
data = pd.read_csv(f'data/{stock}_1YR.csv', usecols=["Open", "Close"])

for num in data["Open"]:
    if ',' in str(num):
        num = float(num.replace(',', ''))

for num in data["Close"]:
    if ',' in str(num):
        num = float(num.replace(',', ''))

# data["Open"] = data["Open"].str.replace(',', '').astype(float)
# data["Close"] = data["Close"].str.replace(',', '').astype(float)

# Drop any rows that have missing values (NaN) after the conversion
data.dropna(inplace=True)

last_index = data.index[0]
data.drop(last_index, inplace=True)

