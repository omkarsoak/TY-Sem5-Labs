def dfs(graph, start, goal):
    open_list = [(start, [start])]
    closed_list = set()

    while open_list:
        current_node, path = open_list.pop()

        if current_node == goal:
            print("Goal found! Path:", path)
            return

        if current_node not in closed_list:
            closed_list.add(current_node)
            neighbors = graph[current_node]

            for neighbor in neighbors:
                if neighbor not in closed_list and neighbor not in [node for node, _ in open_list]:
                    open_list.append((neighbor, path + [neighbor]))

    print("Goal not reachable.")

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['C'],
    'H': ['E']
}

SearchSpace = {'A': ['B', 'D'], 'B': ['C', 'E', 'A'], 'C': ['E', 'B'], 'D': ['A', 'E', 'G'],
               'E': ['B', 'C', 'F', 'I', 'D'], 'F': ['J', 'I', 'E'], 'G': ['D', 'I', 'H'], 'H': ['G', 'J'],
               'I': ['E', 'F', 'J', 'G'], 'J': ['F', 'H', 'I']}

start_node = 'A'
goal_node = 'J'

dfs(SearchSpace, start_node, goal_node)
