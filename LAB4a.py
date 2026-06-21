# - Write a program to implement the Best First Search (BFS) algorithm.

from queue import PriorityQueue

def best_first_search(graph, heuristics, start, goal):
    visited = set()
    pq = PriorityQueue()
    pq.put((heuristics[start], start))
    came_from = {}

    while not pq.empty():
        _, current = pq.get()

        if current == goal:
            # Reconstruct path
            path = [goal]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            path.reverse()
            print("Path:", ' -> '.join(path))
            return

        if current not in visited:
            visited.add(current)
            for neighbor in graph[current]:
                if neighbor not in visited:
                    pq.put((heuristics[neighbor], neighbor))
                    came_from[neighbor] = current

# Example graph with heuristic values
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': []
}
heuristics = {'A': 2, 'B': 1, 'C': 1, 'D': 0}

# Run Best First Search
best_first_search(graph, heuristics, 'A', 'D')



