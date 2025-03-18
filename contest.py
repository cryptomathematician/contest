n = int(input())

for i in range(1,n+1):
    space= (n-i)//2 
    middle = int(n+1/2)
    space_i = i//2 
   
    number = n-i
    while i < middle:
        space*= " " 
        i*= '*'
        print(f"{space}{i}")
    else:
        space_i *=" "
        number*= '*'
        print(f"{space_i}{number}")


