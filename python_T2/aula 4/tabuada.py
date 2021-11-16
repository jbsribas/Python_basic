
#declarar uma lista
multiplos = [1,2,3,4,5,6,7,8,9,10]

try:
    numero = int(input("Digite um numero inteiro dentre 1 a 10: "))

    # verficiação se o numero esta entre 1 e 10, caso não,
    #vai entrar no looping e ficar solicitando o numero correto
    while (numero<0 or numero>10):
        print("Você digitou um numero errado!!")
        numero = int(input("Digite um numero inteiro dentre 1 a 10: "))


    # este o for da tabuada
    for m in range(len(multiplos)+5):
        print(multiplos[m],"*",numero,"=",multiplos[m]*numero)


except ValueError:
    print("Por favor digite somente numeros inteiros")


except:
    print("**"*30)
    print("Ocorreu um erro no processamento do programa")
    print("**"*30)


