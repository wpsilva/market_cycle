import matplotlib.pyplot as plt
import yfinance as yf

# Obter os dados históricos do IBOV para 2024
ibov = yf.download("^BVSP", start='2000-01-01', interval='1mo')
ibov['ano'] = ibov.index.year
# Calcular a variação percentual do IBOV em janeiro e no ano
ibov["variacao_mes"] = ibov["Adj Close"].pct_change()
ibov["variacao_ano"] = ibov["variacao_mes"].groupby(ibov["ano"]).sum()
