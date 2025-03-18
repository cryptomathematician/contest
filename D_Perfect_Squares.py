import math
number_of_numbers = int(input())
numbers = list(map(int, input().split()))

nonsquares_list = []
def check_squared_root(num):
    if num < 0:
        return False
    root = math.isqrt(num)
    if root* root == num:
        return True
    else: 
        return False
    
nonsquares_list = []
for i in numbers :
    if check_squared_root(i) == False :
        nonsquares_list.append(i)

print(max(nonsquares_list))




