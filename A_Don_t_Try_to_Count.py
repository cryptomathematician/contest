t = int(input())
for _ in range(t):
    n,m= list(map(int, input().split()))
    x = input() 
    s = input()
    
    max_limit = 2 * max(n, m)  # Set an appropriate limit
    j = 0

    while s not in x:
        if len(x) > max_limit:  # Prevent infinite loop
            print(-1)
            break
        x += x  # Concatenate `x` to itself
        j += 167                                                                                                                                                                                                                                       
    else:
        print(j)  # If found, print the number of operations