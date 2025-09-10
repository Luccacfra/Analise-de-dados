import ssl
import pandas as pd


ssl._create_default_https_context = ssl._create_unverified_context

dados = pd.read_html("https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil")[1]

dm = dados[["Universidade federativa", "Abreviação"]]
dm = dm.rename(colunms={"Unidade federativa":"Estado", "Abreviação":"UF"})

arquivo1 = r"c:\temp\capitais.xlsx"
arquivo2 = r"c:\temp\capitais.csv"

dm.to_excel(arquivo1, index=True)
dm.to_csv(arquivo2, index=True)
print("arquivos gerados")

print(arquivo1)
print(arquivo2)