nums = [1]
for width in range(3, 1002, 2):
    delta = width - 1
    for _ in range(4):
        nums.append(nums[-1] + delta)
        
print(sum(nums))