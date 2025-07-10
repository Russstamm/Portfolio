from core import AvgAggregator, MinAggregator, MaxAggregator
from core.parser import parse_condition

AGGREGATION_MAP = {
    "avg": AvgAggregator,
    "min": MinAggregator,
    "max": MaxAggregator,
}


def get_aggregator(data: list[dict], column: str):
    column, operand, function = parse_condition(column)
    if function not in AGGREGATION_MAP:
        raise ValueError(f"Unknown function for aggregation: {function}")
    aggregator_class = AGGREGATION_MAP[function]
    return aggregator_class(data, column)
