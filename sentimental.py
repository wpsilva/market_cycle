from transformers import pipeline
from news import News

news_var = News()
news_list = news_var.get_news()
sentiments = []

classifier = pipeline("sentiment-analysis", model="neuralmind/bert-base-portuguese-cased-sentiment")

for title, link in news_list:
    result = classifier(title)
    label = result[0]["label"]
    score = result[0]["score"]
    sentiments.append((label, score))

# Comparar o resultado da análise de sentimentos com a variação do IBOV em janeiro e no ano
labels = [label for label, score in sentiments]
scores = [score for label, score in sentiments]

plt.figure(figsize=(10, 6))
plt.plot(df["Fechamento"]["2024-01"], label="IBOV")
plt.scatter(df.index["2024-01"], scores, c=labels, cmap="RdYlGn", label="Sentimento")
plt.legend()
plt.title("Relação entre o sentimento das notícias e o desempenho do IBOV em janeiro de 2024")
plt.xlabel("Data")
plt.ylabel("Valor")
plt.show()