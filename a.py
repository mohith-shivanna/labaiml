def print_state(state):
    for row in state:
        print(" ".join(map(str, row)))
    print()

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def move_up(state):
    i, j = find_blank(state)
    if i > 0:
        new_state = [row[:] for row in state]
        new_state[i][j], new_state[i-1][j] = new_state[i-1][j], new_state[i][j]
        return new_state
    return None

def move_down(state):
    i, j = find_blank(state)
    if i < 2:
        new_state = [row[:] for row in state]
        new_state[i][j], new_state[i+1][j] = new_state[i+1][j], new_state[i][j]
        return new_state
    return None

def move_left(state):
    i, j = find_blank(state)
    if j > 0:
        new_state = [row[:] for row in state]
        new_state[i][j], new_state[i][j-1] = new_state[i][j-1], new_state[i][j]
        return new_state
    return None

def move_right(state):
    i, j = find_blank(state)
    if j < 2:
        new_state = [row[:] for row in state]
        new_state[i][j], new_state[i][j+1] = new_state[i][j+1], new_state[i][j]
        return new_state
    return None

def calculate_heuristics(state, goal_state):
    h = sum(state[i][j] != goal_state[i][j] for i in range(3) for j in range(3) if state[i][j] != 0)
    return h

def astar_search(initial_state, goal_state):
    OPEN = [(calculate_heuristics(initial_state, goal_state), 0, initial_state)]
    CLOSED = set()
    move_count = 0  # Counter for number of moves

    while OPEN:
        OPEN.sort()  # Ensures lowest-cost state is picked first
        f, g, current_state = OPEN.pop(0)  # Get state with lowest f-score
        CLOSED.add(tuple(map(tuple, current_state)))

        print_state(current_state)

        if current_state == goal_state:
            print(f"Goal Reached in {move_count} moves!")
            return

        successors = [
            (move_up(current_state), "UP"),
            (move_down(current_state), "DOWN"),
            (move_left(current_state), "LEFT"),
            (move_right(current_state), "RIGHT")
        ]
        
        successors = [(s, move) for s, move in successors if s is not None and tuple(map(tuple, s)) not in CLOSED]

        for successor, move in successors:
            h = calculate_heuristics(successor, goal_state)
            g_successor = g + 1
            f_successor = g_successor + h

            if (f_successor, g_successor, successor) not in OPEN:
                OPEN.append((f_successor, g_successor, successor))
        
        move_count += 1  # Increment move counter

    print("No Solution Found")

# Initial and goal states
initial_state = [[1, 2, 3], [4, 7, 5], [0, 6, 8]]
goal_state = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]

# Run A* search
astar_search(initial_state, goal_state)
