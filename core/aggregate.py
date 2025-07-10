class AvgAggregator:
    def __init__(self, data, column):
        self.data = data
        self.column = column

    def aggregate(self):
        values = [float(row[self.column]) for row in self.data if row.get(self.column)]
        return sum(values) / len(values) if values else 0


class MinAggregator:
    def __init__(self, data, column):
        self.data = data
        self.column = column

    def aggregate(self):
        values = [float(row[self.column]) for row in self.data if row.get(self.column)]
        return min(values) if values else None


class MaxAggregator:
    def __init__(self, data, column):
        self.data = data
        self.column = column

    def aggregate(self):
        values = [float(row[self.column]) for row in self.data if row.get(self.column)]
        return max(values) if values else None
