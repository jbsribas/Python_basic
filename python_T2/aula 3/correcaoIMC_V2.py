## correção entrada e saida

nome = input("Qual é o seu nome? ")
alt = float(input("Qual é sua altura (m)? "))
kg = float(input("Qual é o seu peso (Kg)"))
situacao = " "
# calculo 
imc = kg/ (alt*alt) # imc = kg/alt**2

if imc < 17:
    situacao = "Muito abaixo do peso"
elif imc>= 17 and imc <= 18.49:
    situacao = "Abaixo do peso"
elif imc>= 18.50 and imc<= 24.99:
    situacao = "Peso normal"
elif imc>=25 and imc<=29.99:
    situacao = "Acima do peso"
elif imc>= 30 and imc <= 34.99:
    situacao = "Obesidade I"
elif imc>= 35 and imc<= 39.99:
    situacao = "Obesidade II"
else:
    situacao = "Obsediade III"


print("Olá", nome," se IMC é ",round(imc,2),"logo sua situação está",situacao)
