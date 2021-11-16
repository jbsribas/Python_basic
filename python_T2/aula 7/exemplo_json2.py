import pandas as pd
import simplejson as sj

def ler_json(arquivo):
     with open(arquivo, 'r', encoding='utf8') as f:
        return sj.load(f)


dadosj= ler_json("exemplo.json")

print(dadosj)
type(dadosj)

df_j = pd.DataFrame(data=dadosj)
print(df_j)


