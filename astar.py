from queue import PriorityQueue

# Graph representation: adjacency list with edge costs
graph = {
    'A': {'B': 9, 'C': 4, 'D': 7},
    'B': {'A': 9, 'E': 11},
    'C': {'A': 4, 'E': 17, 'F': 12},
    'D': {'A': 7, 'F': 14},
    'E': {'B': 11, 'C': 17, 'G': 5},
    'F': {'C': 12, 'D': 14, 'G': 9},
    'G': {'E': 5, 'F': 9}
}

# Heuristic values (estimated cost from each node to goal G)
# These values are assumed for demonstration and should be consistent and admissible
heuristic = {
    'A': 21,
    'B': 14,
    'C': 18,
    'D': 18,
    'E': 5,
    'F': 8,
    'G': 0
}


def a_star(start, goal):
    open_set = PriorityQueue()
    open_set.put((0 + heuristic[start], start))  # (f_score, node)

    came_from = {}  # To reconstruct path

    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0

    while not open_set.empty():
        current_f, current = open_set.get()

        if current == goal:
            # Reconstruct path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path

        for neighbor, cost in graph[current].items():
            tentative_g_score = g_score[current] + cost
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic[neighbor]
                open_set.put((f_score, neighbor))

    return None  # No path found


# Run the A* algorithm
start_node = 'A'
goal_node = 'G'
path = a_star(start_node, goal_node)

if path:
    print(f"Shortest path from {start_node} to {goal_node} using A* algorithm:")
    print(" -> ".join(path))
else:
    print(f"No path found from {start_node} to {goal_node}.")

