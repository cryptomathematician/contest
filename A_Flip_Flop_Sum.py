number_of = int(input())
for _ in range(number_of):
    number1 = int(input())
    numbers = list(map(int, input().split()))
    total = 0
    maxList = []

    for k in range(len(numbers)-1):
        temp_numbers = numbers[:]
        temp_numbers[k] = -(temp_numbers[k])
        temp_numbers[k+1] = -(temp_numbers[k+1])
        maxList.append(sum(temp_numbers))
    
    print(max(maxList))