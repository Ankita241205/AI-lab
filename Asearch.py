from heapq import heappush, heappop

start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

def heuristic(state):
    return sum(state[i] != 0 and state[i] != goal[i]
               for i in range(9))

def astar(start):
    queue = [(heuristic(start), 0, start, [])]
    visited = set()

    while queue:
        f, cost, state, path = heappop(queue)

        if state == goal:
            return path + [state]

        if state in visited:
            continue
        visited.add(state)

        zero = state.index(0)
        row, col = divmod(zero, 3)

        for move in [-3, 3, -1, 1]:
            new_pos = zero + move

            if 0 <= new_pos < 9:
                if abs(new_pos // 3 - row) + abs(new_pos % 3 - col) != 1:
                    continue

                new_state = list(state)
                new_state[zero], new_state[new_pos] = new_state[new_pos], new_state[zero]
                new_state = tuple(new_state)

                if new_state not in visited:
                    heappush(queue, (
                        cost + 1 + heuristic(new_state),
                        cost + 1,
                        new_state,
                        path + [state]
                    ))

    return None

solution = astar(start)

if solution:
    for state in solution:
        for i in range(0, 9, 3):
            print(state[i:i+3])
        print()
    print("Goal reached!")
else:
    print("No solution found!")



# from heapq import heappush, heappop

# start=()
goal=()
def heuristic(state):
    return sum(state[i] != 0 and state[i] != goal[i]
               for i in range(9))

def astar(start):
    queue=[(heuristic(start), 0, start, [])]
    visited=set()

    while queue:
        f, cost, state, path=heappop(queue)

        if state==goal:
            return path+[state]

        if state in visited:
            continue
        visited.add(state)

        zero=state.index(0)
        row, col=divmod(zero, 3)

        for move in [-3, 3, -1, 1]:
            new_pos=zero + move

            if 0<=new_pos<9:
                if abs(new_pos//3-row) + abs(new_pos%3-col) !=1:
                    continue

                new_state=list(state)
                new_state[zero],new_state[new_pos]=new_state[new_pos],new_state[zero]
                new_state=tuple(new_state)

                if new_state not in visited:
                    heappush(queue, (
                        cost+1+heuristic(new_state), cost+1, new_state, path+[state]
                    ))
    return None

solution = astar(start)

if solution:
    for state in solution:
        for i in range(0, 9, 3):
            print(state[i:i+3])
        print()
    print("goal reached")
else:
    print("no solution found")