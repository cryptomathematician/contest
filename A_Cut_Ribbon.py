def max_ribbon_pieces(n, a, b, c):
    dp = [-1] * (n + 1)  # Initialize DP array with -1 (unreachable states)
    dp[0] = 0  # Base case: 0 pieces for length 0
    
    for i in range(n + 1):
        if dp[i] != -1:  # If current length is achievable
            for x in (a, b, c):
                if i + x <= n:  # Ensure we don't exceed n
                    dp[i + x] = max(dp[i + x], dp[i] + 1)
    
    return dp[n]

# Input Handling
n, a, b, c = map(int, input().split())
print(max_ribbon_pieces(n, a, b, c))