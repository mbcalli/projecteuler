def is_evenly_divisible(n):
    
    for i in range(20, 0, -1):
        if n % i != 0:
            return False
    return True
    
n = 20    
found = False
while not found:
    if is_evenly_divisible(n):
        found = True
    else:
        n += 20

print(n)