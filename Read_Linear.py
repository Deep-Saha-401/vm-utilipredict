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

result_dict = {}
#================================================================
def perform_linear_regression(args_list):
    pathtime,fetch_time=args_list
    file_name = os.path.basename(pathtime)
    data = pd.read_csv(pathtime)
    name1=['CPU']
    item=pd.read_csv(pathtime, names= name1)
    time=fetch_time/5
    y=item[['CPU']]  
    x=item.index.values.reshape(-1, 1)#index   
    x_train,x_test,y_train,y_test=tts(x,y,test_size=0.3)
    reg=LinearRegression()
    reg.fit(x_train,y_train)
    m=reg.coef_
    c=reg.intercept_
    x=time
    y=m*time+c
    return file_name,y

#================================================================
def oppen_linear_regression(main_arg_list):
    pathtime,fetch_time=main_arg_list
    file_name1 = os.path.basename(pathtime)
    if pathtime:
        csv_files = [os.path.join(pathtime, filename) for filename in os.listdir(pathtime)]
        args_list = [(pathtime, fetch_time) for pathtime in csv_files]
        with ThreadPoolExecutor() as executor:
            results = list(executor.map(perform_linear_regression, args_list))

        for file_name, y_values in results:
            result_dict[file_name] = y_values

    return file_name1,result_dict#(20110303,{(vm,CPU_UTIL),(vm,CPU_UTIL)})
#================================================================   
