import pandas as pd

df_bank = pd.read_csv("bank-full.csv",sep=";")
print(df_bank)
print(df_bank.head(5))
print(df_bank.tail(5))
print(df_bank.info())

df_bank.rename(columns={"age":"idade","job":"trabalho"},inplace=True)
print(df_bank)
x = df_bank['idade']
print(type(x))
print(str(x))
print(type(x))

print(df_bank.describe())
print(df_bank.describe(include="O"))
print(df_bank['idade'].describe())
print(df_bank['idade'].describe())

print(df_bank['pdays'].describe())

print("\nserie:\n")
s = pd.Series([1.80,1.70,1.70,1.80,1.75], index=['Matheus','Rodrigo','Gislene','Bruno','Carlos'])
print(s)

#sub data fame o dfatiamento do data frame
df_teste = df_bank[df_bank.idade<40]
print(df_teste)

df_tst = df_bank[['idade','marital','trabalho']]
print(df_tst)

# loc e iloc
#loc
print(df_bank.loc[0:10])

#iloc
print(df_bank.iloc[0:10])

#fatiamento de colunas
print(df_bank.iloc[:,1]) # todas as linhas da ptrimeira coluna

print(df_bank.iloc[:,0:6])# todas as linhas das 6 primeirasc colunas

print(df_bank.iloc[0:5,0:5])# as 5 primeiras linhas das 5 primeiras colunas

print(df_bank.iloc[[10,100,1000],0:5]) # linhas especificas usando uma lista

#fatiamento por coluna no loc
print(df_bank.loc[0:100,['idade','trabalho','education']]) #pega as colunas por nome e as linhas de 0 a 100


# condição mais de uma condição no E = &
df_cond = df_bank[(df_bank.idade<+25) & (df_bank.marital == "single")]
print(df_cond.head(5))





