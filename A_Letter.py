n, m = list(map(int, input().split()))  # Input dimensions n (rows) and m (columns)

j = []
e = []
for _ in range(n):
    row = input()  # Read each row as a string
    e.append(row)  # Append the row to the list `e`


b = []
for i in e:  # Iterate over each row in the grid
    f = []  # List to store indices of '*'
    for k in range(m): 
        if i[k] == "*":  # Check for '*' in the row
            f.append(k)
            b.append(k) # Append the index of '*'

    
    if len(f) == 0:  # If no '*' is found in the row
        print('')  # Print an empty line
    else:
        l = min(b)  # Leftmost index of '*'
        s = max(b)  # Rightmost index of '*'
        print(i[l:s + 1])  # Slice the string from l to s (inclusive)




    
    


    

