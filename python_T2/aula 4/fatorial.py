# calculo do fatorial
try:
    valor= int(input("Digite um numero entre 2 e 15: "))

    while(valor<2 or valor>15):
        print("** Você digitou uma opção incorreta!! **")
        valor= int(input("Digite um numero entre 2 e 15: "))

    fat = 1
    cont = 0

    #calculo fatorial
    while(cont < valor):
        fat = fat*valor
        cont += 1

    #fora do looping
    print("O fatorial de %d é %d"%(valor,fat))

except ValueError:
    print("Digite somente numeros inteiros")

except:
    print("Ocorreu um erro de processamento, tente novamente mais tarde!!")
