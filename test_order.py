import pytest
from order import calculate_total_amount, order_status
def test_calculate_total_amount():
    prices = [100, 200, 300]
    quantities = [1, 2, 3]
    assert calculate_total_amount(prices, quantities) == 100*1 + 200*2 + 300*3  # 1400
    prices = [0, 0, 0]
    quantities = [0, 0, 0]
    assert calculate_total_amount(prices, quantities) == 0
    prices = []
    quantities = []
    assert calculate_total_amount(prices, quantities) == 0
def test_order_status():
    assert order_status(6000) == "Premium Order"
    assert order_status(3500) == "Standard Order"
    assert order_status(1500) == "Basic Order"
    assert order_status(5000) == "Premium Order"
    assert order_status(2000) == "Standard Order"
    assert order_status(1999) == "Basic Order"
