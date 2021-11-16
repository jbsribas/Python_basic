import numpy as np

a = np.array([[4,6,8],[3,5,7]])
b = np.array([[11,13,17],[23,29,31]])

print("raiz cubica A: \n",np.cbrt(a),"\n")
print("raiz cubica de BB\n",np.cbrt(b),"\n")
print("Soma acumulativa de A:\n",a.cumsum())
print("media de A:\n",a.mean(),"\n")
print("media de B:\n",b.mean(),"\n")
print("-B + B:\n",np.negative(b)+b,"\n")


