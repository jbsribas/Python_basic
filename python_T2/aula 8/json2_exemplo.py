import json # Necessário para decodificar o JSON
import pandas as pd
import numpy as np

#Abre o arquivo grades.json
with open('exemplo2.json') as ex:    
  dados = json.load(ex) #Decodifica os dados

#Normaliza os dados contidos na chave students
dt = pd.json_normalize(dados,'students') 

#Cria uma nova coluna e calcula a média dos três exames
dt['média'] = dt.apply(lambda x: np.average([x['exam1'], x['exam2'] , x['exam3']]) , axis=1)
print(dt)