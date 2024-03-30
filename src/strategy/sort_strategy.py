from abc import ABC, abstractmethod


class SortStrategy(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def execute(self) -> list[int]:
        raise NotImplementedError
