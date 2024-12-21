from functools import cache

@cache
def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n == 3:
        return 2
    
    return fib(n-1) + fib(n-2)

n = 1
f = fib(n)
while len(str(f)) < 1_000:
    n += 1
    f = fib(n)
    
print(n)