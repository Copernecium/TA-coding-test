from collections import deque

def find_shortest_path(maze):
    # Directions for up, down, left, right
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    
    # Initialize queue with start position and visited set
    queue = deque([(0, 0)])
    visited = set((0, 0))
    
    # Copy of the maze to modify
    maze_copy = [row[:] for row in maze]
    
    while queue:
        x, y = queue.popleft()
        
        # Check if current cell is the exit
        if maze[x][y] == 3:
            # Update maze with shortest path
            maze_copy[x][y] = 8
            return maze_copy
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # Check if new position is valid
            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] != 1 and (nx, ny) not in visited:
                queue.append((nx, ny))
                visited.add((nx, ny))
                maze_copy[nx][ny] = 8
                
    # No path found
    return None

# Example usage
maze = [
    [1,1,1,1,1],
    [0,0,0,0,0],
    [0,1,2,1,0],
    [0,1,0,1,0],
    [0,0,0,1,3]
]

result = find_shortest_path(maze)
if result is not None:
    print(result)
else:
    print("No path found")
