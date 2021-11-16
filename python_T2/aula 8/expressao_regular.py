import re 
exemplo = 'AV Analytics Vidhya AV' 
#metodo de busca 

#match = Esse método encontra equivalência se ela ocorrer no início da string.
result = re.match(r'AV',exemplo) 
print(result)
print(result.group(0))
print(result.start()) 
print(result.end()) 

result = re.match(r'Analytics',exemplo ) 
print(result)  # retorna vazio pois a string de busca começa com Av e não analitics


#############################################
#find()
print(exemplo.find('AV')) #retorna a posição da primeira letra

print("*"*30)
#faz uma busca em qualquer parte da string
result =re.search(r'Analytics',exemplo ) 
print(result.group(0))

# retorna todas as ocorrencias encontradas em uma lista
result = re.findall(r'AV',exemplo) 
print(result)

# realiza a busca e retorna o valor divido (quebrado ou separado)
#** o analytics era o ponto de quebra
result = re.split(r'Analytics',exemplo ) 
print(result)

exemplo2 = 'AV é a maior comunidade de Analytics da India'
#replace ou substituição do parametro 1 para o parametro 2
result=re.sub(r'da India','do Mundo',exemplo2) 
print(result) 

# compile
print("*"*30)
busca = re.compile("AV")
result = busca.findall(exemplo)
print(result)
result = busca.findall(exemplo2)
print(result)
