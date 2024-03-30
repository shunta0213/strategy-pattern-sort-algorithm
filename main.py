from src.context import SortContext
from src.strategy import SortType

if __name__ == "__main__":
    sort = SortContext([3, 2, 1], SortType.SELECTION)
    print(sort.sort())
