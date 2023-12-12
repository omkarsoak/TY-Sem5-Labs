import math

def euclidean_distance(node1, node2):
    if isinstance(node1, int) and isinstance(node2, int):
        return abs(node1 - node2)
    elif isinstance(node1, tuple) and isinstance(node2, tuple):
        x1, y1 = node1
        x2, y2 = node2
        return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    else:
        raise ValueError("Unsupported node representation")

def simple_hill_climbing(graph, start_node, goal_node):
    current_node = start_node

    while current_node != goal_node:
        neighbors = graph[current_node]
        heuristic_values = {neighbor: euclidean_distance(neighbors[neighbor], graph[goal_node]) for neighbor in neighbors}
        next_node = min(heuristic_values, key=heuristic_values.get)

        if heuristic_values[next_node] >= heuristic_values[current_node]:
            break  # Stuck in a local minimum, exit the loop

        current_node = next_node

    if current_node == goal_node:
        print("Goal node found:", goal_node)
    else:
        print("Goal node not found")


import random

def stochastic_hill_climbing(graph, start_node, goal_node):
    current_node = start_node

    while current_node != goal_node:
        neighbors = graph[current_node]
        heuristic_values = {neighbor: euclidean_distance(neighbors[neighbor], graph[goal_node]) for neighbor in neighbors}

        candidates = [neighbor for neighbor in neighbors if heuristic_values[neighbor] < heuristic_values[current_node]]
        
        if not candidates:
            break  # Stuck in a local minimum, exit the loop

        next_node = random.choice(candidates)
        current_node = next_node

    if current_node == goal_node:
        print("Goal node found:", goal_node)
    else:
        print("Goal node not found")

def steepest_ascent_hill_climbing(graph, start_node, goal_node):
    current_node = start_node

    while current_node != goal_node:
        neighbors = graph[current_node]
        heuristic_values = {neighbor: euclidean_distance(neighbors[neighbor], graph[goal_node]) for neighbor in neighbors}
        
        best_neighbor = min(heuristic_values, key=heuristic_values.get)
        
        if heuristic_values[best_neighbor] >= heuristic_values[current_node]:
            break  # Stuck in a local minimum, exit the loop

        current_node = best_neighbor

    if current_node == goal_node:
        print("Goal node found:", goal_node)
    else:
        print("Goal node not found")

# Example graph represented as a dictionary with coordinates
graph = {
    'A': (0, 0),
    'B': (1, 1),
    'C': (2, 0),
    'D': (1, 2),
    'E': (3, 0),
    'F': (3, 2)
}

start_node = 'A'
goal_node = 'F'

simple_hill_climbing(graph, start_node, goal_node)
