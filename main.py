from src.context import SortContext
from src.strategy import SortType
from src.utils import Utils

if __name__ == "__main__":
    sort_type = SortType.SELECTION
    data = Utils.generate_random_list(50)
    ctx = SortContext(data, sort_type)

    print(ctx.sort())
