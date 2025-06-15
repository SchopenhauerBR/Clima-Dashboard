import requests

def pegar_clima(cidade, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&lang=pt_br&units=metric"
    resposta = requests.get(url)

    if resposta.status_code ==200:
        dados = resposta.json()  # <- Essa linha estava faltando
        clima = {                # <- Aqui o nome correto é clima, não dados
            "cidade": dados["name"],
            "temperatura": dados["main"]["temp"],
            "sensacao": dados["main"]["feels_like"],  # Corrigido: você colocou umidade aqui por engano
            "umidade": dados["main"]["humidity"],
            "descricao": dados["weather"][0]["description"].capitalize(),

        }
        return clima
    else:
        return None