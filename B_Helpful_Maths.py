numbers = input()
lis = [s for s in numbers if s != '+']



list_of_numbers = []
for num in lis: 
     list_of_numbers.append(num)
    
        
sorted_numbers=sorted(list_of_numbers) 
   
print("+".join(map(str, sorted_numbers)))