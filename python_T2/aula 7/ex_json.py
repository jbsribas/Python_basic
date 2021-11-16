import simplejson as sj


d = {"Primiro nome": "Teste",
     "sobrenome": "Lala",
     "titulos":['aha','hehe','ixi']}
     #converte um dicionário
print(sj.dumps(d))

#uma string json  para carregar como dicionario
s ='{"Primiro nome": "Teste","sobrenome ": "Lala"}'
print(s)
print(sj.loads(s))

# convetendo um objeto pyton em string json
print(sj.dumps(d))
