# test_order_processor.py
import pytest
import os
from order_processor import fetch_orders, validate_orders, save_to_json

@pytest.fixture
def mock_item():
    return [
        {"id": 1, "userId": 101},
        {"id": 2, "userId": 102},
        {"id": 3, "userId": 103},
        {"id": 4, "userId": 104}
    ]

def test_orders_api_success(mock_item):
    result = validate_orders(mock_item)
    assert len(result) == 4

def test_orders_invalid_response():
    assert validate_orders([]) == []
    assert validate_orders(None) == []

def test_orders_file_write(mock_item):
    processed = validate_orders(mock_item)
    filename = "test_output.json"
    save_to_json(processed, filename)
    assert os.path.exists(filename)
    if os.path.exists(filename):
        os.remove(filename)

@pytest.mark.xfail
def test_orders_future_feature():
    data = [{"id": 1}]
    result = validate_orders(data)
    assert "tax_amount" in result[0]