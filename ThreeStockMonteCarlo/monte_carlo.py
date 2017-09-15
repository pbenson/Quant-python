import math
import numpy as np
class PriceSeries(object):
    def __init__(self, tckr, prices):
        self.ticker = tckr
        self.price_series = prices
        self.log_returns = [math.log(prices[i]/prices[i+1])
                            for i in range(len(prices) - 1)]

    def __repr__(self):
        return 'PriceSeries(' + self.ticker + ') ' \
               + str(len(self.price_series)) + ' prices'

    def current_price(self):
        return self.price_series[0]

class Scenario(object):
    def __init__(self, num_days_history_used):
        self.weight_on_returns = \
            np.random.normal(0, 1/np.sqrt(num_days_history_used), num_days_history_used)

class Position(object):
    def __init__(self, price_series, num_shares):
        self.price_series = price_series
        self.num_shares = num_shares
        self.profits = []

    def __repr__(self):
        return str(self.num_shares) + ' shares of ' + self.price_series.ticker

    def append_profit(self, profit):
        self.profits.append(profit)

    def profit(self, scenario):
        log_return = np.inner(scenario.weight_on_returns,
                              self.price_series.log_returns[:len(scenario.weight_on_returns)])
        new_price = self.price_series.current_price() * np.exp(log_return)
        price_change = new_price - self.price_series.current_price()
        return price_change * self.num_shares

    def var(self, quantile):
        sorted_profits = sorted(self.profits)
        return -sorted_profits[int(quantile * len(sorted_profits))]


class Portfolio(object):
    def __init__(self):
        self.positions = []

    def add_position(self, price_series, num_shares):
        self.positions.append(Position(price_series, num_shares))

    def __repr__(self):
        return 'Portfolio with ' + str(len(self.positions)) + ' positions'