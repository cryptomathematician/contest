A,B,C = list(map(int, input().split()))

if A==0 and B==0 and C==0:
    print(-1)
elif A==0 and B==0:
    print(0)
elif  A==0 :
    print(1)
    print(f"{-C/B:.10f}")
else:
    D = B**2 - 4*A*C  # Compute discriminant

    if D < 0:
        print(0)  # No real roots
    elif D == 0:
        x = -B / (2*A)
        print(1)
        print(f"{x:.10f}")
    else:
        x1 = (-B + D**0.5) / (2*A)
        x2 = (-B - D**0.5) / (2*A)
        print(2)
        print(f"{min(x1, x2):.10f}\n{max(x1, x2):.10f}")