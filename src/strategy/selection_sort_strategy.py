from .sort_strategy import SortStrategy


class SelectionSortStrategy(SortStrategy):
    def __init__(self, data: list[int]) -> None:
        self._data = data
        super().__init__()

    def execute(self) -> list[int]:
        for i in range(len(self._data)):
            min_index = i
            for j in range(i + 1, len(self._data)):
                if self._data[j] < self._data[min_index]:
                    min_index = j
            self._data[i], self._data[min_index] = self._data[min_index], self._data[i]

        return self._data
