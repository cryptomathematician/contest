s = input()

for i in range(int(s)+1,9000):
    if len(set(str(i))) == 4:
        print(i)
        break

