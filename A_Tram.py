number_of = int(input())
listings = []
for _ in range(number_of):
    n,x= list(map(int, input().split()))
    listings.append(n)
    listings.append(x)

j= listings[0] + listings[1]
 
minimumCapacity = []
minimumCapacity.append(j)
for i in range(2, len(listings)):
    if i%2 == 0:
        j-= listings[i]
        minimumCapacity.append(j)
    else:
        j+= listings[i]
        minimumCapacity.append(j)


print(max(minimumCapacity))