from core.registry import get_aggregator


def test_aggregate_avg():
    rows = [
        {"price": "100"},
        {"price": "200"},
        {"price": "300"},
    ]
    aggregator = get_aggregator(rows, "price=avg")
    result = aggregator.aggregate()
    assert result == 200


def test_aggregate_min():
    rows = [
        {"price": "50"},
        {"price": "200"},
        {"price": "100"},
    ]
    aggregator = get_aggregator(rows, "price=min")
    result = aggregator.aggregate()
    assert result == 50


def test_aggregate_max():
    rows = [
        {"price": "700"},
        {"price": "400"},
        {"price": "900"},
    ]
    aggregator = get_aggregator(rows, "price=max")
    result = aggregator.aggregate()
    assert result == 900
