from tabulate import tabulate
from core import (
    get_aggregator,
    parse_condition,
    ColumnFilter,
    ArgumentParser,
    CsvResource,
)


def main():
    argument_parser = ArgumentParser()
    csv_resource = CsvResource()
    args = argument_parser.parse()
    rows = csv_resource.extract_rows(args.file)

    if args.where:
        try:
            col, op, val = parse_condition(args.where)
            rows = ColumnFilter(rows, col, op, val).apply()
        except Exception as e:
            print(f"Error in filter condition (--where): {e}")
            return

    if args.aggregate:
        try:
            aggregator = get_aggregator(rows, args.aggregate)
            result = aggregator.aggregate()
            header = args.aggregate.split('=')[1]
            print(tabulate([[result]], headers=[header], tablefmt="grid"))
        except Exception as e:
            print(f"Error calculating aggregate (--aggregate): {e}")
            return
    else:
        if rows:
            print(tabulate(rows, headers="keys", tablefmt="grid"))
        else:
            print("No data to display")


if __name__ == "__main__":
    main()
