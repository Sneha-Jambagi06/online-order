from order import order

def test_calculate_total_amount():
    # Test 1: normal case
    prices = [100, 200, 300]
    quantities = [1, 2, 3]
    assert calculate_total_amount(prices, quantities) == 100*1 + 200*2 + 300*3  # 1400

    # Test 2: all zeros
    prices = [0, 0, 0]
    quantities = [0, 0, 0]
    assert calculate_total_amount(prices, quantities) == 0

    # Test 3: empty lists
    prices = []
    quantities = []
    assert calculate_total_amount(prices, quantities) == 0

def test_order_status():
    # Test 1: Premium Order
    assert order_status(6000) == "Premium Order"

    # Test 2: Standard Order
    assert order_status(3500) == "Standard Order"

    # Test 3: Basic Order
    assert order_status(1500) == "Basic Order"

    # Test 4: Boundary cases
    assert order_status(5000) == "Premium Order"
    assert order_status(2000) == "Standard Order"
    assert order_status(1999) == "Basic Order"
