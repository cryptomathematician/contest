

t = int(input())
results = []
for _ in range(t):
    n, m, r, c = list(map(int, input().split()))
    i = (r - 1) * m + c  # Compute the number of the person who leaves
    total_moves = (n * m - i)  # Number of people who move
    wrap_around_count = (total_moves // m)  # Full rows moving up
    result = total_moves + wrap_around_count * (m - 1)
    results.append(str(result))

print("\n".join(results) + "\n")

