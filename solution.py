import requests
from datetime import datetime, timedelta

def cotar():
    cotacao = []
    hoje = datetime.today()

    for dia in range(365):
        data_anterior = hoje - timedelta(days=dia)

        while True:
            data = data_anterior.strftime("%m-%d-%Y")

            url = fr"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao='{data}'&$top=100&$format=json&$select=cotacaoCompra"

            res = requests.get(url)
            res = res.json()

            if res['value']:
                cotacao.append(res['value'][0]['cotacaoCompra'])
                break
            else:
                data_anterior = data_anterior - timedelta(days=1)

    return cotacao
print(cotar())