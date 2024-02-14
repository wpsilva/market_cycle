import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import investpy
from datetime import datetime, timedelta

ticker = "^BVSP"  # IBOV ticker symbol
start_date = "2012-01-20"
end_date = "2024-01-01"
ibov_data = yf.download(ticker, start=start_date, end=end_date)["Adj Close"]

feriados_br = investpy.economic_calendar(countries=['Brazil'], from_date='25/01/2012', to_date='05/01/2024')
feriados_br = feriados_br[feriados_br["time"]=='All Day']
data_objeto = [datetime.strptime(data, '%d/%m/%Y').strftime('%Y-%m-%d') for data in feriados_br["date"].tolist()]

def calculate_returns_around_holidays(data, holiday_dates, window_days=5):
    returns = []
    for holiday in holiday_dates:
        before_window = data[datetime.strptime(holiday, '%Y-%m-%d') - timedelta(days=window_days) : holiday]
        after_window = data[holiday : datetime.strptime(holiday, '%Y-%m-%d') + timedelta(days=window_days)]
        avg_return = (after_window.mean() / before_window.mean()) - 1
        returns.append(avg_return)
    return pd.Series(returns, index=holiday_dates)

holiday_returns = calculate_returns_around_holidays(ibov_data, data_objeto)

overall_avg_return = ibov_data.pct_change().mean()
holiday_avg_return = holiday_returns.mean()

print(f"Retorno médio geral: {overall_avg_return:.4f}")
print(f"Retorno médio durante feriados: {holiday_avg_return:.4f}")