from fractions import Fraction
 

Y, W = list(map(int,input().split()))

r = max(Y,W)

j = 0
for i in range(1,7):
    if i >= r:
        j+=1



frac = Fraction(j, 6) 

if frac == 0:
    print('0/1')
elif frac == 1:
    print('1/1')
else:
    print(frac)


