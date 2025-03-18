s = "0000"

listBinaryOnes= [i for i in s if i!="0"]
k=listBinaryOnes.pop(0)
listBinaryZeros =  [i for i in s if i!="1"]
m= listBinaryOnes + listBinaryZeros + list(k)

result= "" 

for j in m:
    result+=j



print(result)