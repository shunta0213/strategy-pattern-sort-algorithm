import numpy as np


class Utils:
    @staticmethod
    def generate_random_list(n: int) -> list[int]:
        rand_list: list[int] = np.random.randint(0, 1000000, n).tolist()
        return rand_list
