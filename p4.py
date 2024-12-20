class Found(Exception): pass

def is_palindrome(x: int):
    x = str(x)
    for i in range(0, len(x) // 2):
        if x[i] != x[-(i+1)]:
            return False
    return True

largest = -1
for i in range(999, 99, -1):
    for j in range(999, 99, -1):
        product = i * j
        if is_palindrome(product):
            largest = max(largest, product)
            
print(largest)