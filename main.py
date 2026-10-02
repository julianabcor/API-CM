import requests


menu_moedas = """
=== Opções de Moedas para Consulta ===

Tradicionais:

USD-BRL (Dólar Americano)
EUR-BRL (Euro)
GBP-BRL (Libra Esterlina)
ARS-BRL (Peso Argentino)
Criptomoedas:

BTC-BRL (Bitcoin)
ETH-BRL (Ethereum)
=====================================
"""

print(menu_moedas) 

def consultar_moeda(moeda):
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        print("Deu certo!")
        print(resposta.json())
        return resposta.json()
    
    elif resposta.status_code == 404:
        print("Ocorreu um erro.")
        json = resposta.json()
        status = json['status']
        mensagem = json['message']
        codigo = json['code']
        print(f"Status: {status}")
        print(f"Mensagem: {mensagem}")
        print(f"Código do erro: {codigo}")
        return resposta.json()
    
    else:
        print("Deu ruim..")

moeda_desejada = input("Digite a moeda que deseja consultar: ")

dados_api = consultar_moeda(moeda_desejada)

if dados_api:
    valor = dados_api[moeda_desejada]["bid"]
    print("\nRequisição bem-sucedida!")
    print(f"O valor atual de {moeda_desejada} é: ")
    print(f"R$ {float(valor):.2f} ")
else:
    print(f"\nErro ao consultar a moeda: {moeda_desejada}. Verifique se o formato está correto.")