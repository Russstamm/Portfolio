from core import parse_condition


def test_parse_aggregate_arg():
    column, operator, value = parse_condition("price=avg")

    assert column == "price"
    assert operator == "="
    assert value == "avg"


def test_parse_filter_arg():
    column, operator, value = parse_condition("rating>4.5")

    assert column == "rating"
    assert operator == ">"
    assert value == "4.5"
