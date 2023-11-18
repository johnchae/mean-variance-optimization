# mean-variance-optimization
This project uses Python with pandas, numpy, and matplotlib to get datasets of different stock assets and determine the best recommended portfolio for investors. It finds the quarterly returns, expected returns, and covariance of each stock dataset then generates a set of random portfolios along with a set of optimal portfolios, also referred to as an efficient frontier. All results are plotted and visualized.

Script1 takes in a data set of 5 stocks.

Script2 adds 2 more, making 7 total stocks. We compare how this differentiates from the efficient frontier from script1 as well as a new efficient frontier with 2 stocks removed that had the least expected returns.

Script3 adds 3 more, making 10 total stocks. We choose five of the best stocks based on highest expected return with most negative covariance and compare that efficient frontier to the one generated from all ten stocks.
