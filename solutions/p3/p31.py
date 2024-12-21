from tqdm import tqdm

paths = []

for ones in tqdm(range(int(200/1) + 1)):
    for twos in range(int(200/2) + 1):
        for fives in range(int(200/5) + 1):
            for tens in range(int(200/10) + 1):
                if ones + 2 * twos + 5 * fives + 10 * tens > 200:
                    continue
                for twenties in range(int(200/20) + 1):
                    for fifties in range(int(200/50) + 1):
                        for hundreds in range(int(200/100) + 1):
                            for twohundreds in range(int(200/200) + 1):
                                if ones + 2 * twos + 5 * fives + 10 * tens + 20 * twenties + 50 * fifties + 100 * hundreds + 200 * twohundreds == 200:
                                    paths.append((ones, twos, fives, tens, twenties, fifties, hundreds, twohundreds))

print( len( set( tuple(path) for path in paths) ) )