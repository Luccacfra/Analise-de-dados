#read_html()

import ssl
import pandas as pd
import openpyxl 


ssl._create_default_https_context = ssl._create_unverified_context
print("\U0001F697", "Ranking dos carros Eletrificados no Brasil em 2023", "\U0001F50C")

df_montadoras = pd.read_html("https://insideevs.uol.com.br/news/703266/byd-vendas-montadoras-brasil-2023/")[0]
print("\U0001F697", "Inicio gravação dos Arquivo", "\U0001F50C")

print(df_montadoras)

#?
arquivo1 = r"c:\temp\Eletrificados.xlsx"
arquivo2 = r"c:\temp\Eletrificados.csv"

df_montadoras.to_excel(arquivo1,index=True)
df_montadoras.to_csv(arquivo2,index=True)

print(arquivo1)
print(arquivo2)
#?


print("\U0001F697", "Fim gravação dos Arquivo", "\U0001F50C")