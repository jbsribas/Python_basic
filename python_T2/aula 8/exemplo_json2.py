import pandas as pd
import json 

#função para ler o arquivo json
def ler_json(arquivo):
     with open(arquivo, 'r', encoding='utf8') as f:
        return json.load(f)

#função para escrever arquivo json
def escrever_json(dados,nomeArquivo):
    with open(nomeArquivo+'.json', 'w', encoding='utf8') as f:
        json.dump(dados, f, ensure_ascii=False, 
        sort_keys=True, indent=4, separators=(',', ':'))


    






