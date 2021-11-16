import pandas as pd

df =  pd.read_csv("bank-full.csv",sep=";")
print(df.head(5))

#seleção de 4 colunas com o loc pelo nome da coluna
df_selecao = df.loc[:,['age',"default","education","job"]]

print(df_selecao)

#seleção de 4 colunas com o iloc pelo indice da coluna
df_selecao = df.iloc[:,[1,3,4,9]]
print(df_selecao)

#duas colunas as 15 primeiras e duas linhas loc
df_selecao = df.loc[0:14,['age','education']]
print(df_selecao)

# selecionar as 15 primeiras de duas colunas iloc
df_selecao = df.iloc[0:14,[5,16]]
print(df_selecao)

# todos com a idade abaixo de 25 anos
df_selecao = df[df.age<25]
print(df_selecao)

df_selecao = df[df.marital == 'married']
print(df_selecao)

#juntas as duas coisas
df_selecao = df[(df.age<25) & (df.marital == 'married')]
print(df_selecao)
