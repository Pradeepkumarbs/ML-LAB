# - Write a program to implement the A* algorithm.

from queue import PriorityQueue

def a_star(graph, heuristics, start, goal):
    open_set = PriorityQueue()
    open_set.put((heuristics[start], start))
    
    g_cost = {node: float('inf') for node in graph}
    g_cost[start] = 0
    came_from = {}

    while not open_set.empty():
        _, current = open_set.get()

        if current == goal:
            # Reconstruct path
            path = [goal]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            path.reverse()
            print("Shortest Path:", ' -> '.join(path))
            return

        for neighbor, cost in graph[current]:
            new_cost = g_cost[current] + cost
            if new_cost < g_cost[neighbor]:
                g_cost[neighbor] = new_cost
                priority = new_cost + heuristics[neighbor]
                open_set.put((priority, neighbor))
                came_from[neighbor] = current

# Example Graph
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3)],
    'C': [('D', 1)],
    'D': []
}
heuristics = {'A': 4, 'B': 2, 'C': 2, 'D': 0}

# Run A*
a_star(graph, heuristics, 'A', 'D')
