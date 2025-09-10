#dataframe -> Tabela de dados, semelhante ao excel, composto por linhas e colunas onde linhas representam observações ou entradas das tabelas e colunas representam os atributos ou caracteristicas dos dados
#cada coluna do dataframe é na verdade uma série pandas
#utilizar para organizar dados, executar operações complexas, manipular um grande conjunto de dados

#criar um dataframe
import pandas as pd

# dados = {'Nome': ['Ana', 'Bruno', 'Carlos', 'Diana'], 'Idade': [23,25,22,24], 'Nota':[88,92,95,85]}

# df_estudante = pd.DataFrame(dados)
# print(df_estudante)

# print(df_estudante['Nome'])

#.loc ou .iloc
# print("Usando loc para acessar a primeira linha (indice 0):")
# print(df_estudante.loc[0])
# print("Usando iloc para acessar a segunda linha (posição 1):")
# print(df_estudante.iloc[1]) 

#operações e filtrando dados
#filtrando alunos com notas maior que 90

# estudantes_acima = df_estudante[df_estudante['Nota']>90]
# print(estudantes_acima)

#adicionando uma nova coluna
# df_estudante['Passou'] = df_estudante['Nota'] >= 90
# df_estudante['Resultado'] = df_estudante['Nota'].apply(lambda x:'Passou' if x >= 90 else 'Reprovou')
# print(df_estudante)

#limpeza, trasnformação e agragação
dados = {'Nome': ['Ana', 'Bruno', 'Carlos', 'Diana'], 'Idade': [23,25,None,24], 'Nota':[88,92,95,85]}

df_estudante = pd.DataFrame(dados)
print(df_estudante)

media_idade = df_estudante['Idade'].mean()
#preenchendo valores nulos com media
df_estudante.fillna({'Idade':media_idade},inplace=True)
#adicionando coluna aprovado com base na nota
df_estudante['Aprovado'] = df_estudante['Nota']>=90
media_notas = df_estudante['Nota'].mean()

print(df_estudante)
print(f"Média das notas:{media_notas}")
