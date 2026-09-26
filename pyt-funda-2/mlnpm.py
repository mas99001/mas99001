import os
def clear_screen():
    # 'nt' means Windows, otherwise it's likely Linux or macOS
    os.system('cls' if os.name == 'nt' else 'clear')
clear_screen()
## NumPy
import numpy as np
#arr = np.array(21)
#arr = np.array([21])
#arr = np.array([[[1,2,3,4],[1,2,3,4]],[[1,2,3,4],[1,2,3,4]]], dtype='int32')
#print(arr.ndim)
#print(arr.shape)
#rint(type(arr))
#print(arr.dtype)
#print(arr[1:5]) #disply 9,11,14,15
#print(arr[-3:-1]) #disply 15,26
#print(arr[0:3])
'''
arr = np.array([6,9,11,14,15,26,37])
print(arr)
c_arr = arr.copy()
c_arr[0] = 66
print(f'arr is {arr}, id of arr is {id(arr)}')
print(f'c_arr is {c_arr}, id of c_arr is {id(c_arr)}')
filt = [False,True,False,True,False,True,False]
print(arr[filt])
arr3 = np.concatenate([arr,c_arr])
print(arr3)
'''
## Pandas
import pandas as pd
'''
data = [1,2,3,4,5,6]
series = pd.Series(data, index=['A','B','C','D','E','F'])
print(f'Series is\n {series}')
series['G'] = 7
print(f'Series is\n {series}')
dict_4 = {
    'employee':['A','B','C','D','E','F'],
    'department':['DS','DA','SDE','DS','DS','SDE'],
    'salary':[30000,25000,35000,36000,32000,25000]
    }
df4 = pd.DataFrame(data=dict_4)
print()
print(df4)
print(df4.groupby('department').sum().reset_index())
print(df4['salary'].sum())
print(df4['salary'].mean())
'''

data1 = {
    'Person':['A','A','C','B','A'],
    'Rating':[1.8,2.3,3.6,4.5,0.4]
}
df1 = pd.DataFrame(data=data1)
print(df1)
cond = (df1['Person']=='A')
print(df1[cond]['Rating'].mean())
print(df1.groupby('Person').mean())

## Matplotlib

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 6, 10]

plt.plot(x, y)
#plt.savefig('basic_plot.png')
plt.show()

labels_1 = ['A','B','C','D','E']
values = [3,7,5,2,8]
plt.bar(labels_1,values)
plt.show()
plt.pie(values,labels=labels_1)
plt.show()
