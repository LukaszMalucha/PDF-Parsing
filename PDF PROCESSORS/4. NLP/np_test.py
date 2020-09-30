# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 10:23:41 2020

@author: LukaszMalucha
"""

import numpy as np

my_list = [1,2,3,4]

my_array = np.array(my_list)
type(my_array)

matrix = np.array([[4,6,8,7], [20,5,6,9] ])

x = np.random.rand(15)

x = np.random.rand(5,5)


x = np.random.randn(10)



x = np.random.randint(10, 20)


x = np.random.randint(1,100, 16)

x = np.arange(1,50,5)

x = np.eye(15)

x = np.ones(10)

x = np.ones((15,15))



def generate_matrix(x):
    
    arr = np.random.randint(1,x, 20)
    
    return arr

y = generate_matrix(4)



######################################################################## SHAPES

my_list = [-30, 4,50,60,29,15,22,50]

x = np.array(my_list)

len(x)

x.shape

x.dtype

z = x.reshape(2,4)

x.max()

x.min()

x.argmax()

x.argmin()

y = np.arange(300,500,10)

y = y.reshape(4,5)


z = np.random.randint(-1000,1000, (20,20))



################################################################### MATHEMATICS

x = np.arange(1,10)

y = np.arange(1,10)

suma = x + y

squared = x**2

root = np.sqrt(squared)

exp = np.exp(y)

X = np.array([3,20,30])
Y = np.array([4,6,7])

# DISTANCE
Z = np.sqrt(X**2 + Y**2)


################################################################# SLICE & INDEX

import numpy as np


x = np.array([20,40,50,21,15])


x[3]

x[0:3]


x[0:2] = 10

matrix = np.random.randint(1, 10, (5,5))


matrix[2][1]

matrix[:2, 3:] = matrix[:2, 3:]  * 2
mini_matrix = matrix[2:4, 2:4]

mini_matrix[0] = 0


############################################################# ELEMENT SELECTION

import numpy as np

matrix = np.random.randint(1,10, (5,5))

new_matrix = matrix[ matrix > 3]


new_matrix = matrix[ matrix%2!=0]


matrix[ matrix%2==1] = 25
matrix[ matrix%2==0] = 0






































