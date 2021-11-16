########################################################
import numpy as np

#operações com arrays
a = np.array([[1,2],[3,4]])
print("A: ",a,"\n")
print("A*2: ",a*2, "\n")
print("A+3: ",a+3,"\n")
print("A-2: ",a-2,"\n")
print("A/5: ",a/5,"\n")
print("A**2",a ** 2)

# operações entre arrays
b = np.array([[1,2],[3,4]])
print("B: ",b,"\n")
print("A*B: ",a*b, "\n")
print("A+B: ",a+b,"\n")
print("A-B: ",a-b,"\n")
print("A/B: ",a/b,"\n")
print("A**B",a ** b, "\n")

print("A>B: ",a>b, "\n")
print("A==B: ",a==b,"\n")
print("A!=B: ",a!=b,"\n")

#operações entre arrays com tamanhos diferentes
c = np.array([2,3])
d = np.array([[1,2],[3,4]])

print("C: ", c,"\n")
print("D: ", d, "\n")
print("C*3: ", c*3, "\n")
print("D*3: ", d*3, "\n")
print("D*C: ", d*c, "\n")



