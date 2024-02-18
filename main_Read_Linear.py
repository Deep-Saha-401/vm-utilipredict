import Read_Linear
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
import Second_linear_regration

root = Tk()
root.title("VM UTILIZATION FINDER")
root.geometry("400x600")
Over_utilized=[]
Under_utilized=[]
#pathDC = r"D:\MCA_Python\Linear Regression\test dropdown"
pathDC = r"D:\MCA_Python\Linear Regression\exp"
optionsDC=os.listdir(pathDC)
storing_vm_utilization =[]
return_accurate_vm_utilization={}
sorted_VM={}

def pick_time():
    pathtime=pathDC
    print(pathtime)#D:\MCA_Python\Linear Regression\exp
    if pathtime:
        csv_files = [os.path.join(pathtime, filename) for filename in os.listdir(pathtime)]
        fetch_time=int(time_input.get())
        fetch_Upper_Threshold=int(Upper_Threshold_input.get())
        fetch_Lower_Threshold=int(Lower_Threshold_input.get())
        args_list = [(pathtime, fetch_time) for pathtime in csv_files]
        with ThreadPoolExecutor() as executor:
            results = list(executor.map(Read_Linear.oppen_linear_regression, args_list))
         
#================================
        for file_name, y_values in results:           
            for key, value in y_values.items():#[[34.65465]]
                flag=0
                for row_index, row in enumerate(storing_vm_utilization):
                    if str(row[0]) == str(key):
                        V=value[0][0]#[[34.65465]]
                        #print(value)
                        storing_vm_utilization[row_index].append(V)
                        flag=1
                if (flag==0):
                    V=value[0][0]
                    new_row = [key,V]
                    storing_vm_utilization.append(new_row)


    fetch_day=int(Day_input.get())
    return_accurate_vm_utilization=Second_linear_regration.second_Linear_regression(storing_vm_utilization,fetch_day)


    for row_index, row in enumerate(return_accurate_vm_utilization):
        x=return_accurate_vm_utilization[row][0][0]
        if fetch_Lower_Threshold <= x and x <= fetch_Upper_Threshold:
            sorted_VM[row]=x
            
    print('=====Fitness Checked VM ========')
    print(sorted_VM)
    sorted_dict = dict(sorted(sorted_VM.items(), key=lambda item: item[1]))
    #print('=====sorted_dict ========')
    #print(sorted_dict)
    fetch_no_of_VM=int(no_of_VM.get())
    count = 0
    print('=====Ultimate Sorted VM ========')
    for key, value in sorted_dict.items():
        print(key, value)
        count += 1
        if count == fetch_no_of_VM:
            break
#================================    
# Enter TIME 
time=Label(root,text='Enter Time')
time.pack(pady=(20,5))
time.config(font=('verdana',12))
time_input=Entry(root,width=50)
time_input.pack(ipady=2,pady=(1,5))

# Enter UPPER Threshold 
time=Label(root,text='Enter Upper Threshold')
time.pack(pady=(20,5))
time.config(font=('verdana',12))
Upper_Threshold_input=Entry(root,width=50)
Upper_Threshold_input.pack(ipady=2,pady=(1,5))

# Enter LOWER Threshold 
time=Label(root,text='Enter Lower Threshold')
time.pack(pady=(20,5))
time.config(font=('verdana',12))
Lower_Threshold_input=Entry(root,width=50)
Lower_Threshold_input.pack(ipady=2,pady=(1,5))

# Enter Day
time=Label(root,text='Enter Day')
time.pack(pady=(20,5))
time.config(font=('verdana',12))
Day_input=Entry(root,width=50)
Day_input.pack(ipady=2,pady=(1,5))

# Enter Number of VM 
time=Label(root,text='Enter Number of VM')
time.pack(pady=(20,5))
time.config(font=('verdana',12))
no_of_VM=Entry(root,width=50)
no_of_VM.pack(ipady=2,pady=(1,5))
#------------------------------------------------------------
btn=Button(root,text='Done',bg='white',fg='black',width='8',height='2',command=pick_time)
btn.pack(pady=(20,20))
btn.config(font=('verdana',12))
    
root.mainloop()


