from typing import Dict


exemplo = "Isso é uma String"
exemplo2 = 'Isso também é uma string'
exemplo3 = input("Digite um valor qualquer")

print("variavel exemplo tem o tamanho: ", len(exemplo))
print("um pedaço da string", exemplo[2:7])

###################################################################################
#Lista

lista = [] #lista em branco ou vazio
l = ["banana",'maracujá',"melancia","manga"]
l1 = ["Patricia",47,"abobrinha", 3.14, 1+1j]

print(type(lista))
print(lista)
print(l)
print(l1)
listaG =[lista,l,l1] 
print("lista de listas", listaG)

lista.append("batata") # colocar um novo elemento ao final da lista
lista.insert(0,"chuchu") # colcoar em uma posição especifica
lista.pop() # remove o ultimo elemento colocado
lista.remove("chuchu") # remove a primeira instancia da palavra chuchu

# quebra de string por um parametro => saida em lista
nome = 'Jessica Barbara da Silva Ribas'
exemplo = nome.split(" ")
print(exemplo)


#transformação de uma lista em string
compras = ", ".join(l[len(l)-2])
compras = compras +" "+ "e ".join(l[len(l)-1])
print(compras)

#tuplas
tupla1 = (1,"lALALAALAL")
tupla2 = (2, "lerolerolero")
tupla3 = (3, "lerolerolero")
print(" Minha tupla 1:", tupla1, "\n", "Minha tupla 2",tupla2)

# dicionario
teste  = [tupla1, tupla2, tupla3]
print(teste)
testeDic = dict(teste)
print(testeDic)

#dicionario do exemplo
t1 = ("nome", "Tania")
t2 = ("idade", 35)
t3 = ("fruta", "Uva")
t4 = ("cor", "roxo")
t5 = ("musica", "pop")

#lista de tuplas, para poder criar o dicionario
lista_tuplas = [t1,t2,t3,t4,t5]
print(lista_tuplas)

#criar o dicionario
cadastro = dict(lista_tuplas)
print(cadastro)

#editar o valor
cadastro['fruta'] = "maracujá"
print(cadastro["fruta"])
print(cadastro)

# incluir um novo item
cadastro["sobrenome"] = "Carvalho"
print(cadastro)
print(cadastro["nome"],cadastro["sobrenome"])

#elimitar itens do cidionario -- função del
del cadastro["musica"]
print(cadastro)

# atualizar o dicionario -- função update
cadastro.update({'nome':"Ana", 'idade':27, "fruta":"pera"})
print(cadastro)