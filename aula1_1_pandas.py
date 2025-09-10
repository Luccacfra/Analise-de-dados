import pandas as pd

#lista
cidades = ["São Paulo", "Rio de Janeiro", "Juiz de fora"]
indices = [1,2,3]
serie_cidades = pd.Series(cidades, index=indices)
# print(serie_cidades)

#convert maisculas

cidades_maisculas = serie_cidades.str.upper()
# print(cidades_maisculas)

serie_cidades_string = serie_cidades.astype('string')
# print(serie_cidades_string)

# print(serie_cidades_string)
# print(serie_cidades_string.dtype)

#Determinando o comprimento maximo das cidades para justificar
max_len = max(serie_cidades.str.len())
#justificando os nomes das cidades
series_cidades_alinhadas = serie_cidades.str.ljust(max_len)
for idx, cidade in series_cidades_alinhadas.items():
    print(f"{idx} {cidade}")

    series_cidades_alinhadas = serie_cidades.str.rjust(max_len)
for idx, cidade in series_cidades_alinhadas.items():
    print(f"{idx} {cidade}")

    series_cidades_alinhadas = serie_cidades.str.center(max_len)
for idx, cidade in series_cidades_alinhadas.items():
    print(f"{idx} {cidade}")

    