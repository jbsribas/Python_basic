#### pandas
import pandas as pd
import numpy as np

idade = pd.Series([15,21,30,16,9,54])
print(idade)
print(idade.index) # aqui é para ver o indice
print(idade.values) # ver somente os valores sem o indice

#########
#data frame
#converter um array para data frame
df = pd.DataFrame(np.array([[1,2,3],[4,5,6]]),
                  columns=["a",'b',"c"])
print("DF:\n",df,"\n")

#dicionario
dados = {"valor1":[1,2],"valor2":[3,4],"valor3":[5,6]}
df2 = pd.DataFrame(data = dados)
print(df2)