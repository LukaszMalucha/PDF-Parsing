# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 16:10:10 2020

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

def normalize(df):
    x = df.copy()
    for i in x.columns[1:]:
        x[i] = x[i]/x[i][0] 
        
    return x  


# Random Seeds

np.random.seed(101)

weights = np.array(np.random.random(9))

weights = weights / np.sum(weights)



dataset_portfolio = normalize(dataset)


dataset_portfolio.columns[1:]



for counter, stock in enumerate(dataset_portfolio.columns[1:]):
    dataset_portfolio[stock] = dataset_portfolio[stock] * weights[counter]
    dataset_portfolio[stock] = dataset_portfolio[stock] * 1000000
















