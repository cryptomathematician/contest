from collections import Counter

def findOriginalArray(changed):
    if len(changed) % 2 != 0:
        return []  # If the length is odd, it can't be a doubled array

    freq = Counter(changed)  # Count occurrences
    changed.sort()  # Sort to process smaller numbers first
    original = []

    for num in changed:
        if freq[num] == 0:  # If this number is already used, skip it
            continue
        if freq[num * 2] == 0:  # If there is no double, it's invalid
            return []
        
        original.append(num)  # Add num to original
        freq[num] -= 1  # Use one occurrence of num
        freq[num * 2] -= 1  # Use one occurrence of num * 2

    return original

# Example test cases
print(findOriginalArray([1, 3, 4, 2, 6, 8]))  # Output: [1, 3, 4]
print(findOriginalArray([6, 3, 0, 1]))  # Output: []
print(findOriginalArray([1]))  # Output: []











# changed= [1,3,4,2,6,8]

# original= []
# m = []

# w= len(changed)/2 

# changed.sort()  
# temp = changed[:] 
# for i in temp:
#     k= 2*i
#     if len(set(changed))%2 == 1:
#         if k in changed:
#             m.append(i)
#             changed.remove(i)
#             changed.remove(k)
#     else:
#         if k in changed:
#             m.append(i)
#             changed.remove(k)

# if len(m)== w :
#     print(m)
# else:
#     print([])

# changed= [0,3,2,4,6,0]
# original= []
# m = []

# w= len(changed)/2 
# for i in changed:
#     k= 2*i
#     if k in changed:
#         m.append(i)
#         changed.remove(k)

# if len(m)== w :
#     print(m)
# else:
#     print([])



    # if i%2 == 0:
    #     l= []
    #     for k in changed:
    #         if k %2 == 0:
    #             if i%k == 0:
    #                l.append(k)
    #     if len(l)== 1 :
    #         original.append(i)
    # else:
    #     original.append(i)
        



# for i  in  changed:
#     if i%2 == 0:
#         even_of_original.append(i)
#         changed.remove(i)

# original = []
# for i in even_of_original:
#     k= i//2
#     original.append(k)


# if  original.sort() == changed.sort() :
#     print(changed.sort())
# else:
#     print([])

