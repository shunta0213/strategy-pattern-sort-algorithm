from .sort_strategy import SortStrategy


class BubbleSortStrategy(SortStrategy):
    def __init__(self, data: list[int]) -> None:
        self._data = data
        super().__init__()

    def execute(self) -> list[int]:
        for i in range(len(self._data)):
            for j in range(len(self._data) - 1):
                if self._data[j] > self._data[j + 1]:
                    self._data[j], self._data[j + 1] = self._data[j + 1], self._data[j]

        return self._data
