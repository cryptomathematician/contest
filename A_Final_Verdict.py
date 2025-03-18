number_of = int(input())
for _ in range(number_of):
    n,x= list(map(int, input().split()))
    a = list(map(int, input().split()))
    total_sum = sum(a)
    print("YES" if total_sum % n == 0 and total_sum // n == x else "NO")