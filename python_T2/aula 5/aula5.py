import numpy as np
from numpy.core.fromnumeric import ndim

data1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
data2 = np.array([[1,2,3,4],[4,5,6,7],[7,8,9,10]])
data3 = np.array([[1],[2],[3],[4],[5]])
data4 = np.array([1,2,3,4,5])

# shape seria a forma quantidade de dados + dimensões
print(data1.shape)
print(data2.shape)
print(data3.shape)
print(data4.shape)

# len tamanho dos dados ou melhor a quantidade de dados uma dimensão
# pois a quantidade de dados devem ser iguais em todas as dimensões

print(len(data1))

#ndim indica a quantidade de dimensões de um array

print(data3.ndim)
print(data1.ndim)

#a quantidade de elementos dentro do array
print("tamanho",data1.size)
print(data2.size)
print(data3.size)
print(data4.size)

# reshape
print(data2,"\n")
print(data2.reshape(2,6),"\n")
print(data2.reshape(6,2),"\n")
print(data2.reshape(4,3),"\n")

# flatten deixe o array multidimensional em unidimensional
lista1 = [1,2,3,4,5]
lista2 = [6,7,8,9,10]
dim2 = np.array([lista1,lista2])
dim2_2 = np.array([dim2[dim2==3], dim2[dim2 == 4],
                 dim2[dim2 == 8], dim2[dim2 == 9]])

print(dim2_2)
print(dim2_2.shape)

dim1 = dim2_2.flatten()
print(dim1)
print(dim1.shape)


#transpose transpor um array 
# o que é linha vira coluna e o que coluna vira linha
print("**"*30)
print(data1,"\n")
print(data1.transpose())

