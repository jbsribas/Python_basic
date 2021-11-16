import numpy as np


lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
data = np.array(lista)
print(data)

data_3 = np.array([data[data ==4],data[data==6], data[data==8], data[data==10]])
print(data_3)

# remoção dos itens da lista
data_2 = data[data != 4]
data_2 = data_2[data_2 != 6]
data_2 = data_2[data_2 != 8]
data_2 = data_2[data_2 != 10]

print(data_2)

# array de duas dimensões
lista1 = [1,2,3,4,5]
lista2 = [6,7,8,9,10]

dim2 = np.array([lista1,lista2])
print(dim2)

#3,4,8,9

dim2_2 = np.array([dim2[dim2==3], dim2[dim2 == 4],
                 dim2[dim2 == 8], dim2[dim2 == 9]])
print(dim2_2)





