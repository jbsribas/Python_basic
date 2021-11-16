import pandas as pd
import json
# Criar uma função que escreve um arquivo .json
def escrever_json(dados,nome):
    with open(nome+'.json', 'w', encoding='utf8') as f:
        json.dump(dados, f, ensure_ascii=False, sort_keys=True,
         indent=4, separators=(',', ':'))

####################################################################
# Exemplo  de um dicionário que virará um arquivo .json
dict = {"Compras": [{"Mes": "Jan",
                    "Arroz_KG": 5,
                    "Feijão_KG": 1, 
                     "Macarrao_pct": 1, 
                     "Molho_pct": 3},
                    {"Mes": "Fev", 
                    "Arroz_KG": 0, 
                    "Feijão_KG": 0,
                     "Macarrao_pct": 3, 
                     "Molho_pct": 9}]
    }


# codigo principal
escrever_json(dict,"compras")