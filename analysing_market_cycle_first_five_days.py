import yfinance as yf
import numpy as np
import pandas as pd

ibov = yf.download("^BVSP", start="2000-01-01", end="2024-01-01")

ibov["variacao"] = ibov["Adj Close"].pct_change()
ibov = ibov.dropna()
# Criar uma coluna para indicar se o dia foi positivo ou negativo
ibov["positivo"] = ibov["variacao"] > 0

ibov["ano"] = ibov.index.year

ibov_janeiro = ibov[ibov.index.month == 1]
# Verificar se os primeiros cinco dias de trading de janeiro foram positivos para cada ano
january_barometer = ibov_janeiro.groupby("ano").apply(lambda x: x["variacao"].iloc[:5].sum())
performance_anual = ibov.groupby("ano")["variacao"].sum()
resultado = np.where((january_barometer * performance_anual > 0), 1, 0)
df = pd.DataFrame({"janeiro": january_barometer, "ano": performance_anual, "resultado": resultado})
percentual_ocorrencias = df["resultado"].value_counts(normalize=True) * 100
print(df)
print(percentual_ocorrencias)