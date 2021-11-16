## correção entrada e saida

nome = input("Qual é o seu nome? ")
alt = float(input("Qual é sua altura (m)? "))
kg = float(input("Qual é o seu peso (Kg)"))

# calculo 
imc = kg/ (alt*alt) # imc = kg/alt**2

print("Olá %s, seu IMC é %f"%(nome,round(imc,2)))
