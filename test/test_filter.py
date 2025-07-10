import pytest
from core.filter import ColumnFilter
from core import parse_condition


def test_filter_rating_gt():
    rows = [
        {"name": "iphone", "rating": "4.9"},
        {"name": "poco", "rating": "4.4"},
    ]

    # Парсим фильтр
    column, operator, value = parse_condition("rating>4.5")

    # Применяем фильтр
    filtered = ColumnFilter(rows, column, operator, value).apply()

    assert len(filtered) == 1
    assert filtered[0]["name"] == "iphone"
