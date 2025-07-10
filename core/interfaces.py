from abc import ABC, abstractmethod
from typing import List, Dict


class Filter(ABC):
    @abstractmethod
    def apply(self, rows: List[Dict[str, str]]) -> List[Dict[str, str]]:
        pass


class Aggregator(ABC):
    @abstractmethod
    def compute(self, rows: List[Dict[str, str]]) -> float:
        pass
