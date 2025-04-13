import timeit

def benchmark_clean(text: str, iterations: int = 1000) -> float:
    """Measure cleaning speed."""
    return timeit.timeit(lambda: clean_text(text), number=iterations)
