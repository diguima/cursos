import requests
import os
import json

print("Início")

API_KEY = "AIzaSyD_Ran-U1NSQYOG4KdxAX6qcbo2ylhZ89Y"
MODEL_NAME = "gemini-1.5-flash-latest"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL_NAME}:generateContent?key={API_KEY}"

request_body = {
    "contents": [
        {
            "parts": [
                {
                    "text": "dê uma lista aleatória de 20 palavras"
                }
            ]
        }
    ]
}

# Send the POST request with JSON content
response = requests.post(
    URL, headers={'Content-Type': 'application/json'}, json=request_body)

# Check for successful response
if response.status_code == 200:

    responseJSON = response.json()

    print(type(responseJSON))

    # Caminho do diretório e do arquivo
    # diretorio = 'c:\\tmp'
    # arquivo = os.path.join(diretorio, 'palavras.json')

    # Cria o diretório se ele não existir
    # os.makedirs(diretorio, exist_ok=True)

    # Conteúdo do arquivo
    # conteudo = "Este é um exemplo de conteúdo para o arquivo."

    # Cria e escreve no arquivo
    # with open(arquivo, 'w', encoding='utf-8') as f:
    #     # f.write(conteudo)
    #     f.write(json.dumps(wordsList))

    counter = 0

    keysValues = []

    for key, value in responseJSON.items():

        valueType = type(value)

        keysValues.append(value)

    for key in keysValues:

        if type(key) == 'dict':

            listObj = key.json()
            

        # print(key)
        # print(type(key))
        
else:

    print(f"Error: {response.status_code}")
    print(response.text)