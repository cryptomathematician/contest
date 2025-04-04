number_of = int(input())
numbers = list(map(int, input().split()))
k = max(numbers)
r = numbers.index(k)+1


if r%4 == 1:
    print("chest")
elif r%4 == 2:
    print("biceps")
elif r%4 == 3:
    print("back")