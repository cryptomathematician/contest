def max_typing_time_string(s):
    n = len(s)
    best_time = 0
    best_string = ""

    # Try inserting each letter ('a' to 'z') at every position
    for i in range(n + 1):
        for c in "abcdefghijklmnopqrstuvwxyz":
            new_s = s[:i] + c + s[i:]  # Insert letter 'c' at position 'i'
            
            # Calculate typing time
            time = 2  # First character takes 2 seconds
            for j in range(1, len(new_s)):
                if new_s[j] == new_s[j - 1]:
                    time += 1
                else:
                    time += 2
            
            # Update best result
            if time > best_time:
                best_time = time
                best_string = new_s

    return best_string

# Read input
t = int(input())
for _ in range(t):
    s = input().strip()
    print(max_typing_time_string(s))
