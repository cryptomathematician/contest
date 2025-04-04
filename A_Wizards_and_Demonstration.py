from math import ceil

# Read input values
n, x, y = map(int, input().split())

# Compute the required number of participants
required_people = ceil((y / 100) * n)

# Compute the number of clones needed
clones_needed = max(0, required_people - x)

# Print the result
print(clones_needed)



