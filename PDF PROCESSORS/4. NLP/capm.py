# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 17:55:55 2020

@author: LukaszMalucha
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from copy import copy
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go


def normalize(df):
    x = df.copy()
    for i in x.columns[1:]:
        x[i] = x[i] / x[i][0]
    return x
    

def daily_return(df):
    df_daily_return = df.copy()
    for i in df.columns[1:]:
        for j in range(1, len(df)):
            df_daily_return[i][j] = ( df[i][j] - df[i][j-1] / df[i][j-1] ) * 100
        
        df_daily_return[i][0] = 0
        
    return df_daily_return    
    



dataset = pd.read_csv("stock.csv", encoding="utf-8")

dataset = dataset.sort_values(by="Date")

dataset = normalize(dataset)

# DAILY RETURN CALCULATION

dataset_daily_return = daily_return(dataset)


dataset_daily_return.mean()



# BETA 


dataset_daily_return["AAPL"]



dataset_daily_return.plot(kind = "scatter", x = 'sp500', y = 'AAPL')




beta, alpha = np.polyfit(dataset_daily_return['sp500'], dataset_daily_return['AAPL'], 1)



# CAPM - relationship between the expected return and risk of securities - CAPITAL ASSETS PRICING MODEL














