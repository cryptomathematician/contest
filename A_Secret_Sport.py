t = int(input())
for _ in range(t):
    n= int(input())
    s = input()

    sets_won = {"A": 0, "B": 0}
        
    current_set_A = 0
    current_set_B = 0
    
    for ch in s:
        if ch == 'A':
            current_set_A += 1
        else:
            current_set_B += 1
        
        if current_set_A > 0 and current_set_A == current_set_B + 1:
            sets_won["A"] += 1
            current_set_A, current_set_B = 0, 0
        elif current_set_B > 0 and current_set_B == current_set_A + 1:
            sets_won["B"] += 1
            current_set_A, current_set_B = 0, 0
    
    if sets_won["A"] > sets_won["B"]:
        print("A")
    elif sets_won["B"] > sets_won["A"]:
        print("B")
    else:
        ("?")