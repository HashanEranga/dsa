from factorial import factorial

def test_factorial_10(benchmark):
    """
    Test the factorial function with a known input and output.
    :param benchmark: pytest-benchmark fixture
    """
    result = benchmark(factorial, 10)
    assert result == 3628800, f"Expected 3628800 but got {result}"

def test_factorial_100(benchmark):
    """
    Test the factorial function with a larger input.
    :param benchmark: pytest-benchmark fixture
    """
    result = benchmark(factorial, 100)
    assert result > 0

def test_factorial_500(benchmark):
    """
    Test the factorial function with a very large input.
    :param benchmark: pytest-benchmark fixture
    """
    result = benchmark(factorial, 500)
    assert result > 0