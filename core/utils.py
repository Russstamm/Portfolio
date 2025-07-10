OPERATORS = {
    ">=": lambda c: c.split(">="),
    "<=": lambda c: c.split("<="),
    ">": lambda c: c.split(">"),
    "<": lambda c: c.split("<"),
    "=": lambda c: c.split("="),
}


def parse_condition(condition: str) -> tuple[str, str, str]:
    for operand, splitter in OPERATORS.items():
        if operand in condition:
            column, value = splitter(condition)
            return column.strip(), operand, value.strip()
    raise ValueError("Invalid condition format")
