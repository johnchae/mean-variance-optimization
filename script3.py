import pandas as pd
import matplotlib.pyplot as plt
from rf import return_portfolios, optimal_portfolio
import numpy as np

# 3 assets added to script2's stock data (10 total)
path='stock_data3.csv'
stock_data = pd.read_csv(path)

selected = list(stock_data.columns[1:])
returns_quarterly = stock_data[selected].pct_change()
expected_returns = returns_quarterly.mean()
cov_quarterly = returns_quarterly.cov()

print(expected_returns)
print(cov_quarterly)

# Choosing the best 5 assets based on highest expected return with most negative covariance
selected = ['TGT', 'CVS', 'M', 'VZ', 'JPM']
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

single_asset_std=np.sqrt(np.diagonal(cov_quarterly))
plt.scatter(single_asset_std,expected_returns,marker='X',color='red',s=200)

# All 10
all_ten_EF = pd.read_csv('all_ten.csv')
plt.plot(all_ten_EF['Risks'], all_ten_EF['Returns'], 'g-o')

plt.show()
