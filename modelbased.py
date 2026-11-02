grid=[['S','.','#'],
      ['#','.','.'],
      ['.','.','G']]


position=[0,0] #starting position
visited=set()

while grid[position[0]][position[1]] != 'G':
    x,y=position
    visited.add((x,y))

    moves=[(x+1, y), (x, y+1), (x-1,y), (x, y-1)]

    moved=False
    for nx, ny in moves:
        if (0<=nx<len(grid) and 
            0<=ny<len(grid[0]) and
            grid[nx][ny] != '#' and 
            (nx, ny) not in visited):

            position=nx,ny
            moved=True
            break

    if not moved:
        print("goal not reached")
        break

    print("current position:", position)

if (grid[position[0]][position[1]] == 'G'):
    print("goal reached")

print("internal state(visiteed cells):", visited)


