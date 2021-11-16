### colcoar as importações no começo do script

import numpy as np
import math

######################################################

lista = [1,2,3,4,5]
k = np.array(lista) # conversão da lista em um array unidimencional
print("Unidimensiona :: uma dimensão")
print(k)
print("**"*30)


dois = np.array([lista,lista]) # isso é um array de duas faces ou dimensões
print("Bidimensional :: duas dimensões")
print(dois)
print("**"*30)

tres = np.array([[lista,lista],
                [lista,lista]])
print("Tridimensional :: três dimensões")
print(tres)
print("**"*30)
##########################################################

#função zeros e ones

zero = np.zeros([2,2,2]) # tridimensional
print(zero)

um = np.ones([2,2]) #bidimensional
print(um)

teste = np.arange(10)
print(teste)
test_c = teste.copy()
print(test_c)

test = test_c[0:3] #slice , corte utilizando os indices e salvar e outra variavel
print(test_c, test)


test = teste[teste>4]
print(test)

test = teste[teste == 4]
print(test)

test = teste[teste!= 4]
print(test)





