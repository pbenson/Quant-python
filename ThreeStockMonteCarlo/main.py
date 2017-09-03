# print('hello, world')

import csv
import monte_carlo as mc

with open('AMZN_GOOG_AAPL.csv', 'r') as csvfile:
    price_reader = csv.reader(csvfile, delimiter=',')
    on_first_row = True
    # all_price_series = []
    for row in price_reader:
        if on_first_row:
            tickers = row[1:]
            ticker_to_prices_dict = {ticker: [] for ticker in tickers}
            on_first_row = False
        else:
            prices = row[1:]
            for ticker, price in zip(tickers, prices):
                ticker_to_prices_dict[ticker].append(float(price))

    # ticker_to_series_dict = {}
    # for ticker, prices in ticker_to_prices_dict.items():
    #     # all_price_series.append(mc.PriceSeries(ticker, prices))
    #     ticker_to_series_dict[ticker] = mc.PriceSeries(ticker, prices)
    ticker_to_series_dict = {ticker:mc.PriceSeries(ticker, prices)
                             for ticker, prices in ticker_to_prices_dict.items()}

    num_simulations = 10
    num_days_history_used = 252
    scenarios = [mc.Scenario(num_days_history_used)
                 for _ in range(num_simulations)]
    portfolio = mc.Portfolio()
    portfolio.add_position(ticker_to_series_dict['AMZN'], 1000)
    portfolio.add_position(ticker_to_series_dict['AAPL'], 2000)
    portfolio.add_position(ticker_to_series_dict['GOOG'], -1000)


    for scenario in scenarios:
        for position in portfolio.positions:
            profit = position.profit(scenario)
            profit