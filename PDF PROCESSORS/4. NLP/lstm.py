# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 15:04:51 2020

@author: LukaszMalucha
"""



import pandas as pd
import numpy as np
from scipy import stats
from tensorflow import keras
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from copy import copy


dataset = pd.read_csv("stock.csv", encoding="utf-8")

dataset_volume = pd.read_csv("stock_volume.csv", encoding="utf-8")



dataset = dataset.sort_values(by="Date")
dataset_volume = dataset_volume.sort_values(by="Date")



def individual_stock(price_df, vol_df, name):
    return pd.DataFrame({"Date": price_df['Date'], 'Close': price_df[name], 'Volume':vol_df[name]})


# Create target column for comparison (previous day to today)
def trading_window(data):
    n = 1
    data["Target"] = data[['Close']].shift(-n)
    return data


price_volume_df = individual_stock(dataset, dataset_volume, "AAPL")

price_volume_target_df = trading_window(price_volume_df)

price_volume_target_df = price_volume_target_df.iloc[:-1, :]


# SCALE


from sklearn.preprocessing import MinMaxScaler


sc = MinMaxScaler(feature_range = (0,1))

price_volume_target_scaled_df = sc.fit_transform(price_volume_target_df.drop(columns = ['Date']))

price_volume_target_scaled_df.shape


# XY 

X = price_volume_target_scaled_df[:, :2]
y = price_volume_target_scaled_df[:, 2]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.35, random_state = 0)



## Ridge Regression

#from sklearn.linear_model import Ridge
#
#regression_model = Ridge()
#regression_model.fit(X_train, y_train)
#
#lr_accuracy = regression_model.score(X_test, y_test)
#
#predicted_prices = regression_model.predict(X)

## LSTM


X = np.asarray(X)
y = np.asarray(y)


X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))
X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

X_train.shape[1] 
X_train.shape[2]  


inputs = keras.layers.Input(shape = (X_train.shape[1], X_train.shape[2]))


x = keras.layers.LSTM(150, return_sequences=True)(inputs)
x = keras.layers.LSTM(150, return_sequences=True)(x)
x = keras.layers.LSTM(150, return_sequences=True)(x)
outputs = keras.layers.Dense(1, activation='linear')(x)


model = keras.Model(inputs = inputs, outputs = outputs)
model.compile(optimizer = 'adam', loss = 'mse')
model.summary()












































