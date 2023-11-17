import pandas as pd
import matplotlib.pyplot as plt
from rf import return_portfolios, optimal_portfolio
import numpy as np

# Stock data with only 5 assets
stock_data = pd.read_csv('stock_data_weak.csv')
print(stock_data)

selected = list(stock_data.columns[1:])
returns_quarterly = stock_data[selected].pct_change()
expected_returns = returns_quarterly.mean()
cov_quarterly = returns_quarterly.cov()

random_portfolios = return_portfolios(expected_returns, cov_quarterly)

weights, returns, risks = optimal_portfolio(returns_quarterly[1:])

random_portfolios.plot.scatter(x='Volatility', y='Returns', fontsize=12)
plt.plot(risks, returns, 'y-o')

plt.ylabel('Expected Returns',fontsize=14)
plt.xlabel('Volatility (Std. Deviation)',fontsize=14)
plt.title('Efficient Frontier', fontsize=24)

try:
  single_asset_std=np.sqrt(np.diagonal(cov_quarterly))
  plt.scatter(single_asset_std,expected_returns,marker='X',color='red',s=200)
except:
  pass
plt.show()
