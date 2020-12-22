from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    max_profit, min_buy = 0, prices[0]
    for i in prices:
        min_buy = min(min_buy, i)
        max_profit = max(max_profit, i - min_buy)
    return max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
