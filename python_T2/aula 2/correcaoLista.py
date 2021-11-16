futebol = ["Palmeiras","Santos", "São Paulo", "Corinthas"]
print(futebol)
print(futebol[3])

futebol2 = ["Bahia","Vasco","Cruzeiro"]
futebol3 = ["Guarani","Portuguesa","Ponte Preta"]
print("1 divisao:", futebol)
print("2 divisao: ", futebol2)
print("3 divisao",futebol3)
todos = ["divisao 1:", futebol, " divisao 2: ", futebol2,"divisao 3: ",futebol3]
print(todos)

########
print("**"*30)
moedas = ['dolar','euro','real']
print(moedas)
moedas.append('libra')
print(moedas)
moedas.append('peso')
print(moedas)

print(moedas[len(moedas)-2])
moedaS = ", ".join(moedas)
print(moedaS)
volta = moedaS.split(", ")
print(volta)


