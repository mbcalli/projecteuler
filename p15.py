rows = cols = 20

dp = [[0 for _ in range(rows + 1)] for _ in range(cols + 1)]
dp[0][0] = 1

for r in range(rows+1):
    for c in range(cols+1):
        if r > 0:   
            dp[r][c] += dp[r-1][c]
        if c > 0:
            dp[r][c] += dp[r][c-1]
        
print(dp[rows][cols])