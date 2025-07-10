def parse_condition(condition: str) -> tuple[str, str, str]:
    for operand in [">=", "<=", ">", "<", "="]:
        if operand in condition:
            column, value = condition.split(operand)
            return column.strip(), operand, value.strip()
    raise ValueError(f"Incorrect condition: {condition}")
