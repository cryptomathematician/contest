n = input()
number_of = int(input())
lis=[]
string_i= ""
string_k =""

for _ in range(number_of):
    letters= input()
    lis.append(letters)
        
for i in range(len(n)):
    string_i+=lis[i]
    for j in range(len(n)-1,1,-1):
        string_k+=lis[i]

print(string_k+string_i)



       
if n in lis:
    print("YES")
else:
    print("NO")



