def factorial(n):
    """
    calculate the factorial of a given number
    :param n: number given for finding the factorial
    :return: factorial of the given number n
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    elif n < 0:
        raise ValueError("Factorial is not defined for negative integers.")
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)