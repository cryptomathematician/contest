t = int(input())  # Number of test cases
for _ in range(t):
    n = int(input())
    # Count of full cycles (each cycle has exactly 3 occurrences)
    count = (n // 15) * 3
    # Count extra valid numbers from the remainder range (0, 1, 2)
    count += sum(1 for i in range(n % 15 + 1) if i % 3 == i % 5)
    print(count)
