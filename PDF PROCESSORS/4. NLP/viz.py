# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 13:55:19 2020

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




dataset = pd.read_csv("stock.csv", encoding="utf-8")


print(len(dataset.columns) - 1)


## AVG Return of S&P500
summary = dataset.describe()
dataset.mean()
dataset.std()
dataset["AMZN"].max()


## Explore
nulls = dataset.isnull()

dataset.info()


def show_plot(df, fig_title):
    df.plot(x = "Date", figsize = (15,7), linewidth = 3, title = fig_title)
    plt.grid()
    plt.show()
    
    
show_plot(dataset, "Plot")

def normalize(df):
    x = df.copy()
    for i in x.columns[1:]:
        x[i] = x[i]/x[i][0] 
        
    return x    

def show_plot_normalized(df, fig_title):
    df.plot(x = "Date", figsize = (15,7), linewidth = 3, title = fig_title)
    plt.grid()
    plt.show()
    
    
show_plot_normalized(normalize(dataset), "Plot")


def interactive_plot(df, title):
    fig = px.line(title = title)
    
    for i in df.columns[1:]:
        fig.add_scatter(x=df['Date'], y=df[i], name=i)
        
    
    fig.show()
    
    
interactive_plot(dataset, "Prices")













































