from helper import is_prime

n = 0
count = 0
while count < 10_001:
    n += 1
    if is_prime(n):
        count += 1
        
print(n)