import requests
import json
import urllib3

#Arreglo de urls a checkear
urls = ["https://short.graficonorte.cl","https://www.google.cl"]

#Configurar bot telegram
telegram_url = "https://api.telegram.org/bot/sendMessage"

#Recorrer arreglo y realizar request de prueba
for url in urls:
    try:
        response = requests.get(url,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'})
    except requests.exceptions.RequestException as e:
        print(e)
        sys.exit(1)
    
    #Evaluar que estado sea 200 o 301 (redirect)
    if response.status_code not in [200,301]:
        data = {
            "chat_id": {-1001541076284},
            "text": f"Sitio {url} esta con problemas, codigo de error {response.status_code}"
        }

        try:
            response = requests.post(telegram_url, data=data)
        except requests.exceptions.RequestException as e:
            print(e)
            sys.exit(1)