import concurrent.futures
from concurrent.futures import ThreadPoolExecutor
import pandas as pd
import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split as tts
from functools import partial
import fitness_func

result_dict = {}
def second_Linear_regression(vm_utilization,days):
    for row in vm_utilization:
        name = row[0]
        values = row[1:]
        # Use values as 'y' and the index of values as 'x'
        y = pd.DataFrame(values, columns=['CPU'])
        y2=y.CPU.values.reshape(-1,1)
        x = y.index.values.reshape(-1, 1)
        x_train,x_test,y_train,y_test=tts(x,y,test_size=0.3)
        reg=LinearRegression()
        reg.fit(x_train,y_train)
        m=reg.coef_
        c=reg.intercept_
        #x=time
        y1=m*days+c
        accuracy_percentage=fitness_func.fitness_function(y1,y2)
        if(accuracy_percentage>80):
            result_dict[name] = y1

    return result_dict
