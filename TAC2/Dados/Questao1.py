## ITEM 1
#importando biblioteca
import sys
import pandas as pd
# para chamar no prompt de comando (terminal)
tabela = sys.argv[1]
coef_m = float(sys.argv[2])
coef_b = float(sys.argv[3])
# ITEM 2
df = pd.read_csv(tabela)
# TEM 3
#criando uma nova tabela
df_q = df[['Target_Name','Stage']].drop_duplicates()
#adicionando uma nova coluna
df_q['Quantity'] = 10 ** ((df['CT']-coef_b)/coef_m)
#ITEM 4
#juntando as tabelas
df_final = pd.merge(df,df_q)
#ITEM 5
# salvar a nova tabela:
df_final.to_csv("C:\Users\\beatr\Desktop\PROG\progbiociencia\TAC2\Amostras\Tabela_beatriz.csv")
#ITEM 6
print(df_final)
#chamando terminal
#python Questao1.py C:\Users\beatr\Desktop\PROG\progbiociencia\TAC2\Amostras\Valores_CT.csv -3.397186047 58.53223295

