# Read input grid (3x3)
grid = [list(map(int, input().split())) for _ in range(3)]
print(grid)

# Initialize result grid with all lights ON
result = [[1] * 3 for _ in range(3)]
print(result)

# Direction vectors for adjacent neighbors (left, right, up, down)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# Iterate through the 3x3 grid
for i in range(3):
    for j in range(3):
        # Count total number of toggles including neighbors
        toggle_count = grid[i][j]
        print(toggle_count)
        
        # Check all 4 possible adjacent neighbors
        for d in range(4):
            ni, nj = i + dx[d], j + dy[d]
            if 0 <= ni < 3 and 0 <= nj < 3:  # Ensure within bounds
                toggle_count += grid[ni][nj]

        # Determine final state: odd = OFF (0), even = ON (1)
        result[i][j] = 0 if toggle_count % 2 else 1

# Print final result
for row in result:
    print("".join(map(str, row)))
