import numpy as np

data = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
print(data, "\n")

print("a dimensão: ", data.ndim)
print("Qtde elementos: ", data.size)
print("A forma: ", data.shape,"\n")

# criar novo utilizando o data
data2 = data.reshape(4,4)
print(data2,"\n")

print("a dimensão: ", data2.ndim)
print("Qtde elementos: ", data2.size)
print("A forma: ", data2.shape,"\n")

# driar um array transposto

data_t = data2.transpose()
print(data_t,"\n")

# usar o flatten no transposto

data_flat = data_t.flatten()
print(data_flat)

print(data, "\n")

print(data==data_flat)
print(data==17)




