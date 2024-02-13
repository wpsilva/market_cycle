import matplotlib.pyplot as plt
import yfinance as yf
import numpy as np

# Obter os dados históricos do IBOV para 2024
ibov = yf.download("^BVSP", start='2000-01-01', interval='1mo')
ibov['ano'] = ibov.index.year
# Calcular a variação percentual do IBOV em janeiro e no ano
ibov["variacao_mes"] = ibov["Adj Close"].pct_change()
ibov = ibov.dropna()
ibov["variacao_ano"] = ibov.groupby(ibov.index.year)["variacao_mes"].transform("sum")
#print(ibov["variacao_mes"].iloc[0:11].sum())

# Filtrar apenas os dados de janeiro
ibov_janeiro = ibov[ibov.index.month == 1]

ibov_janeiro['resultado'] = np.where((ibov_janeiro['variacao_mes'] * ibov_janeiro['variacao_ano'] > 0), 1, 0)

percentual_ocorrencias = ibov_janeiro['resultado'].value_counts(normalize=True) * 100

print(percentual_ocorrencias)