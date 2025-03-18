
name= input()

list_of_name = set(list(name))

if len(list_of_name)%2 == 1:
    print('IGNORE HIM!')
else:
    print('CHAT WITH HER!')