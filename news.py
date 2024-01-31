import requests

class News():

    def __init__(self) -> None:
        arquivo = open("API_KEY.txt", "r")
        self.api_key = arquivo.read()
        self.news = []

    def get_news(self):
        endpoint = "https://newsapi.org/v2/everything"

        params = {
            "q": "ibovespa",
            "from": "2000-01-01",
            "to": "2000-01-31",
            "language": "pt",
            "sortBy": "publishedAt",
            "apiKey": self.api_key
        }
        
        response = requests.get(endpoint, params=params)

        if response.status_code == 200:
            data = response.json()
            self.news = data["articles"]
        else:
            print(f"Código de erro: {response.status_code}")
            print(f"Mensagem de erro: {response.text}")