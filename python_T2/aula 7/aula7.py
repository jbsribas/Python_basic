import pandas as pd
from pandas.io.parsers import read_csv, read_table

# criar data frame
dados = {"valor1":[1,2], "valor2":[3,4],"valor3":[5,6]}
df_dados = pd.DataFrame(data=dados)
print(df_dados)

df3 = pd.DataFrame(data=dados, index=['a','b'])
print(df3)

print(df3.values) # visualizar somente valores
print(df3.index) # visualizar indice
print(df3.columns) # visualizar colunas

# importando arquivo csv

#x = pd.read_csv("Economist_pensions.csv",sep=",")
#print(x)
#z = pd.read_excel("C:/Users/jessi/Documents/Matriz de confusao.xlsx")
#print(z)

y = pd.read_csv("iris.csv", sep=",")
print(y)
print(type(y))

f = pd.read_table("teste.txt")
print(f)

print(y.head())
print(y.tail())

y.columns = ["sepala largura","sepala altura","petala altura","petala largura","classe"]

print(y.head(5))

y.rename(columns={"sepala largura":"sl", "sepala altura":"sa"}, inplace=True)
print(y.head(5))

print(y.info())
print(y.describe())
print(y.describe(include=['O']))