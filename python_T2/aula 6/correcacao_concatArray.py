import numpy as np

a= np.array([[1,2,3],[4,5,6]])
b= np.array([[2,4,6,8],[10,12,14,16]])
c = np.array([[11,13,17],[23,29,31]])
d = np.array([[13,14,15],[19,21,23]])
#print("a_b:\n", np.concatenate((a,b)),"\n")
#print("b_c:\n",np.concatenate((b,c)),"\n")
print("b_c eixo1:\n",np.concatenate((b,c),axis=1),"\n")
print("a_d:\n",np.concatenate((a,d)),"\n")
print("a_d:\n",np.concatenate((a,d), axis=1),"\n")
