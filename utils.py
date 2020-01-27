
def clamp(min_value: int, max_value: int, value: int) -> int:
    return max(min(value, max_value), min_value)
