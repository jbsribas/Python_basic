import numpy as np
import pandas as pd

#series
#parece arrays

tst = pd.Series([1,2,3,4,5])
print(tst)

#dataFrame
#pode-se criar tanto por meio de array quanto por dicionario

df =pd.DataFrame(np.array([[1,2,3],[4,5,6],[7,8,9]]), columns=['a','b','c']) 

print(df)

ex = pd.read_csv('Economist_pensions.csv', sep=';')
print(ex.head())

ex2 = pd.read_csv('iris.csv',sep=',')
print(ex2)