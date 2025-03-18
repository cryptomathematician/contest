number_of = int(input())
for _ in range(number_of):
    numbers = list(map(int, input().split()))
    print(numbers)
    numbers_i = []
    result =[]
    for i in range(int(numbers[0]),int(numbers[1]+1)):
        numbers_i.append(i)
        m = str(i)
        j =[int(i) for i in m]
        difference = max(j)-min(j)
        result.append(difference)
    hello = [numbers_i[id] for id,num in enumerate(result) if num== max(result)]
    print(max(hello))