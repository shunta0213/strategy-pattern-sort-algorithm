from src.context import SortContext
from src.strategy import SortType
from src.utils import Utils

if __name__ == "__main__":
    data = Utils.generate_random_list(1000)
    sort = SortContext(data, SortType.SELECTION)
    print(sort.sort())
