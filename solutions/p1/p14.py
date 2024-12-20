from functools import cache

@cache
def collatz(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    if n % 2 == 0:
        return 1 + collatz(n/2)
    else:
        return 1 + collatz(3 * n + 1)
    
largest = -1
largest_idx = None
for i in range(1, 1_000_000):
    collatz_i = collatz(i)
    if collatz_i > largest:
        largest = collatz_i
        largest_idx = i
    
print(largest_idx, largest)