from csv import DictReader


class CsvResource:
    def extract_rows(self, filename: str) -> list:
        with open(filename, encoding="utf-8") as file:
            return list(DictReader(file))
