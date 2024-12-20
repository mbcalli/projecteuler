from functools import cache

@cache
def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return fib(n-1) + fib(n-2)

fibs = [1]
n = 2
while fibs[-1] < 4_000_000:
    fibs.append(fib(n))
    n += 1
    
print(sum(x for x in fibs if x < 4_000_000 and x % 2 == 0))