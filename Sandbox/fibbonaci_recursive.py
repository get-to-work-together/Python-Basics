from functools import lru_cache


@lru_cache
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# Example usage
for i in range(100):
    print(fibonacci(i))
