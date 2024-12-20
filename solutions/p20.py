from functools import cache

@cache
def factorial(n):
    if n == 0 or n == 1:
        return 1
    if n == 2:
        return 2 
    return n * factorial(n - 1)

print(sum(list(map(int, str(factorial(100))))))