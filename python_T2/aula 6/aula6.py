import numpy as np

a = np.array([[1,2],[3,4]])
print("A: ",a,"\n")

print("raiz quadrada:\n",np.sqrt(a),"\n")
print("exponencial:\n", np.exp(a),"\n")
print("negativo:\n",np.negative(a),"\n")
print("Seno:\n ",np.sinc(a),"\n")

#estatistica
print("media:",a.mean(),"\n")
print("mediana:",np.median(a),"\n")
print("minimo:",a.min(),"\n")
print("max:",a.max(),"\n")
print("soma:",a.sum(),"\n")
print("soma pelo np:",np.sum(a),"\n")
print("Soma Acumulativa:",a.cumsum(),"\n")

# concatenação de array

d = np.array([1,2])
print("D: ",d)
e = np.array([3,4,5,6,7])
print("E: ",e)
f = np.array([8,9,10])
print("F: ",f)
g = np.concatenate((d,e))
print("G: ",g)
print("f_e_d_g = ",np.concatenate((f,e,d,g)))

b = np.array([[5,6],[7,8]])
print("a_b axis=0: \n", np.concatenate((a,b)))

# colocando o eixo
print("a_b axis=1 : \n", np.concatenate((a,b),axis=1))


h = np.array([[[5,6],[7,8]],[[5,6],[7,8]]],float)
print("H:\n",h,"\n")

i = np.array([[[1,1],[3,4]],[[1,2],[3,4]]],float)
print("I:\n",i,"\n")

print("h_i:\n",np.concatenate((h,i),axis=0),"\n")
print("h_i axis = 1:\n",np.concatenate((h,i),axis=1),"\n")

