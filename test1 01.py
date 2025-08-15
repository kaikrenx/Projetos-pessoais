import pandas as pd
import os
from twilio.rest import Client
account_sid = "YOUR TWILIO ACCOUNT SID"
auth_token = "YOUR TWILIO AUTH TOKEN"
client = Client(account_sid, auth_token)

lista_meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho"]

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f"{mes}.xlsx")
    if (tabela_vendas["Vendas"] > 55000).any():
        Vendedor = tabela_vendas.loc[tabela_vendas["Vendas"] > 55000, "Vendedor"].values[0]
        Vendas = tabela_vendas.loc[tabela_vendas["Vendas"] > 55000, "Vendas"].values[0]
        print(f"No mês {mes} encontrou alguem bateu a meta. Vendedor: {Vendedor}, Vendas: {Vendas}")



        client.api.account.messages.create(
         to="DESTINED",
        from_="+XXXXXXXXXXXX",
        body= f"No mês {mes} encontrou alguem bateu a meta. Vendedor: {Vendedor}, Vendas: {Vendas}"
     )


