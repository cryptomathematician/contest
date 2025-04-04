n, k = list(map(int, input().split()))
numbers = list(map(int, input().split()))

threshold = numbers[k - 1]

# Count participants who qualify
advancers = sum(1 for score in numbers if score >= threshold and score > 0)

print(advancers)






