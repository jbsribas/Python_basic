# for para percores listas


from ast import increment_lineno


for i in range(0,10):
    print("o numero é :", i)

print("***"*30)

frutas = ["abacate", "amora", "melancia", "melão", "maça"]

for f in frutas:
    print(f); # mostra o elemento da lista na posição atual

print("***"*30)
for f in range(len(frutas)): # trabalhar com variaveis de controle inteira
    print(frutas[f]) # indico qual é o indice da lista que eu quero mostrar


listaN = [1,3,8,7,9]

soma = 0
for k in range(len(listaN)):
     soma += listaN[k]

print("a soma de todos os elementos da lista é:", soma)

texto = ""
for i in range(len(frutas)):
    if(i == len(frutas)-1):
        texto = texto+" e "+frutas[i]
    else:
        if i== 0:
            texto = frutas[i]
        else:
            texto = texto+", "+frutas[i]

print(texto)
#while com variavel de controle
print("***"*30)
cont = 0
while(cont<=10):
    print("o valor da variavel de controle é", cont)
    cont += 1 # invremenetar ou decrementar manualmente dentro looping

#while com break
while(True):
    num = int(input("Digite um numero inteiro: "))
    if num == 5:
        print("você acertou")
        break ## interromper o laço de repetição 
    print("Você errou, tente novamente")

print("Finalmente saiu do laço while")




