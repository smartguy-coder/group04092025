from functools import lru_cache


@lru_cache()
def get_number_powered(number: int) -> int:
    print("get_number_powered was called")
    return number ** 2

