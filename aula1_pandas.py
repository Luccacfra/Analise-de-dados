import pandas as pd

#dados frutas
precos = [1.20,0.5,2.50]

#indices correspondentes
frutas = ['Maça', 'Banana', 'Cereja']

#criando a Série
serie_frutas = pd.Series(precos,index=frutas)

#Preço Maça
preco_maca= serie_frutas['Maça']
# print(f"Preço da maça:{preco_maca}")

preco_banana = serie_frutas['Banana']
# print(f"o preço da banana é:{preco_banana}")

#SOMA DO PREÇOS e MEDIA
preco_total = serie_frutas.sum()
# print(preco_total)
preco_media = serie_frutas.mean()
# print(preco_media)

#filtrando dados de uma série
#frutas com preço maior que 1.0
frutas_caras = serie_frutas[serie_frutas>1.0]
frutas_baratas = serie_frutas[serie_frutas<1.0]
frutas_caras_form = frutas_caras.map('R${:.2f}'.format)
# print(frutas_caras_form)

