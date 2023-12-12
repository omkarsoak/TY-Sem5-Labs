import heapq

#A star is a type of BFS using priority queue
def astar(graph, start, goal):
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {start: None}
    g_score = {start: 0}

    while open_set:
        current_cost, current_node = heapq.heappop(open_set)

        if current_node == goal:
            path = reconstruct_path(came_from, goal)
            return path

        for neighbor, cost in graph[current_node].items():
            tentative_g_score = g_score[current_node] + cost
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score, neighbor))
                came_from[neighbor] = current_node

    return None

def reconstruct_path(came_from, current_node):
    path = [current_node]
    while current_node in came_from and came_from[current_node] is not None:
        current_node = came_from[current_node]
        path.append(current_node)
    return path[::-1]

def heuristic(node, goal):
    # Replace this with your own heuristic function
    return 0

# Example usage:
graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'A': 1, 'D': 4, 'E': 2},
    'C': {'A': 3, 'F': 5},
    'D': {'B': 4},
    'E': {'B': 2, 'F': 1},
    'F': {'C': 5, 'E': 1}
}

start_node = 'A'
goal_node = 'F'

result = astar(graph, start_node, goal_node)
print("Path:", result)
