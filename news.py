import requests
from GoogleNews import GoogleNews

class News():

    def __init__(self) -> None:
        arquivo = open("API_KEY.txt", "r")
        self.api_key = arquivo.read()
        self.news = []
        self.googlenews = GoogleNews(lang='pt',region='BR', start='01/01/2020', end='02/31/2020', encode='utf-8')
        self.googlenews.enableException(True)

    def get_google_news(self):
        self.googlenews.get_news('ibovespa')
        self.news = self.googlenews.results()

        return self.news

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
            return []
        
        return self.news