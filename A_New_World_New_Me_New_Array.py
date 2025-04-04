def min_operations(n, k, p):
    
    if k < -n * p or k > n * p:
        return -1
    
    
    abs_k = abs(k) 
    ops = abs_k // p 
    if abs_k % p != 0:
        ops += 1  
    
    return ops

t = int(input()) 
results = []

for _ in range(t):
    n, k, p = map(int, input().split())  
    results.append(str(min_operations(n, k, p)))


print("\n".join(results))
