#analise de dados veiculos mais vendidos 1° semestre 2024
import pandas as pd

print("\U0001F697" * 38)

dados_veiculos = {'Veiculo': ['Polo', 'Strada', 'Onix', 'HB20', 'Argo'], 'Marca': ['Volkswagen', 'Fiat', 'Chevrolet', 'Hyundai', 'Fiat'],
                  'Preço': [87990, 115995, 97390, 84390, 91990]}
df_veiculos = pd.DataFrame(dados_veiculos)

#formatar preço para moeda real
def formatar_preco(preco):
    return f"R${preco:,.2f}".replace(',','X').replace('.',',').replace('X','.')

df_veiculos['Preço_formatado'] = df_veiculos['Preço'].apply(formatar_preco)

print(df_veiculos)

#filtrando veiculos com preço acima de R$ 110.000,00
df_preco_faixa_1 = df_veiculos[df_veiculos['Preço']>110000]

print("\U0001F697" * 38)
print(df_preco_faixa_1)
print("\U0001F697" * 38)
df_preco_faixa_2 = df_veiculos[(df_veiculos['Preço']>90000) & (df_veiculos['Preço']<= 110000)]
print(df_preco_faixa_2)
print("\U0001F697" * 38)
df_preco_faixa_3 = df_veiculos[(df_veiculos['Preço']<90000)]
print(df_preco_faixa_3)

