import pandas as pd
import json 

from exemplo_json2 import escrever_json,ler_json

# código principal
dadosj= ler_json("entrada/exemplo.json")

print(dadosj)
print(type(dadosj))

# transforma o arquivo json numa estrutura de data frame 
dsj = pd.json_normalize(dadosj,'Funcionario')
print(dsj)

x = dsj.to_dict()
print(x)

escrever_json(x,"result/funcionario")

#salvar o data frame em csv
nomeArquivo = "result/funcionario"
dsj.to_csv(nomeArquivo+'.csv',sep=";", encoding='utf-8')
#sep = separador desejado no caso escolhi o ;
#o encoding é para suportar os acentos e caracteres especiais utilizados em pt-br


