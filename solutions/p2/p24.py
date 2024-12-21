from itertools import permutations

perms = [x for x in permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])]
print(''.join(list(map(str, perms[1_000_000 - 1]))))