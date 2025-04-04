n = int(input())
a = list(map(int, input().split()))
m = int(input())
q = list(map(int, input().split()))

# Sort in descending order
sorted_a = sorted(a, reverse=True)

# Compute prefix sum
prefix_sum = [0] * (n + 1)
for i in range(1, n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + sorted_a[i - 1]



# Answer queries in O(1)
for i in q:
    print(prefix_sum[n]- sorted_a[i - 1])  # Sum of elements except the i-th largest

