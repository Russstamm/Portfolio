from typing import Callable

COMPARISON_MAP: dict[str, Callable[[any, any], bool]] = {
    "=": lambda a, b: a == b,
    ">": lambda a, b: a > b,
    "<": lambda a, b: a < b,
    ">=": lambda a, b: a >= b,
    "<=": lambda a, b: a <= b,
}


class ColumnFilter:
    def __init__(self, rows, column, operator, value):
        self.rows = rows
        self.column = column
        self.operator = operator
        self.value = value

    def apply(self):
        if self.operator == ">":
            return [
                row for row in self.rows if float(row[self.column]) > float(self.value)
            ]
        elif self.operator == "<":
            return [
                row for row in self.rows if float(row[self.column]) < float(self.value)
            ]
        elif self.operator == "=":
            return [
                row for row in self.rows if str(row[self.column]) == str(self.value)
            ]
        else:
            raise ValueError(f"Unsupported operator: {self.operator}")
