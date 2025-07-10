import argparse


class ArgumentParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self._setup_arguments()

    def _setup_arguments(self):
        self.parser.add_argument("--file", required=True)
        self.parser.add_argument("--where")
        self.parser.add_argument("--aggregate")

    def parse(self):
        return self.parser.parse_args()
