from src.strategy import SortStrategy, SortType


class SortContext:
    def __init__(
        self,
        data: list[int],
        sort_type: SortType,
    ) -> None:
        self._data = data
        self._sort_type = sort_type

    def sort(self) -> list[int]:
        strategy = self.__get_strategy()
        return strategy.execute()

    def __get_strategy(self) -> SortStrategy:
        if self._sort_type == SortType.SELECTION:
            from src.strategy import SelectionSortStrategy

            return SelectionSortStrategy(self._data)
        elif self._sort_type == SortType.BUBBLE:
            from src.strategy import BubbleSortStrategy

            return BubbleSortStrategy(self._data)
