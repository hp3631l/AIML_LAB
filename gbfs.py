import heapq

graph = {
    'A': [('B', 1), ('C', 1), ('D', 1)],
    'B': [('E', 1), ('F', 1)],
    'C': [('F', 1)],
    'D': [('G', 1)],
    'E': [('G', 1)],
    'F': [('G', 1)],
    'G': []
}
heuristic = {
    'A': 40,
    'B': 32,
    'C': 25,
    'D': 35,
    'E': 19,
    'F': 17,
    'G': 0
}
def greedy_best_first_search(start, goal):

    visited = set()
    priority_queue = []

    heapq.heappush(priority_queue, (heuristic[start], start, [start]))

    while priority_queue:

        h, current, path = heapq.heappop(priority_queue)

        if current == goal:
            return path

        if current not in visited:
            visited.add(current)

            for neighbor, cost in graph[current]:
                if neighbor not in visited:
                    heapq.heappush(
                        priority_queue,
                        (heuristic[neighbor], neighbor, path + [neighbor])
                    )

    return None
result = greedy_best_first_search('A', 'G')

print("Path found:", " -> ".join(result))
