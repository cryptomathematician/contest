t = int(input())
numbers = list(map(int, input().split()))
n = [i for i in numbers if i%2 == 0]
m = [i for i in numbers if i%2 == 1]



if len(m)== 1:
   print(numbers.index(m[0])+1)

elif len(n)== 1:
    print(numbers.index(n[0])+1)