def dfs(maze, start, end):
    stack = [start]
    visited = set()
    parent = {}

    while stack:
        x, y = stack.pop()

        if (x, y) in visited:
            continue

        visited.add((x, y))

        if (x, y) == end:
            path = []
            while (x, y) != start:
                path.append((x, y))
                x, y = parent[(x, y)]
            path.append(start)
            return path[::-1]

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy

            if (0 <= nx < len(maze) and
                0 <= ny < len(maze[0]) and
                maze[nx][ny] == 0 and
                (nx, ny) not in visited):

                stack.append((nx, ny))
                parent[(nx, ny)] = (x, y)

    return None

maze = [
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [1, 1, 0, 0],
    [0, 0, 0, 0]
]

start = (0, 0)
end = (3, 3)

path = dfs(maze, start, end)

if path:
    print("Path found:", path)
else:
    print("No path found")
