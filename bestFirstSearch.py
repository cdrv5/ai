import heapq

def best_first_search(graph, start, goal):
    explored, frontier = set(), [(0, [start])]
    while frontier:
        _, path = heapq.heappop(frontier)
        current = path[-1]
        if current == goal: return path
        if current not in explored:
            explored.add(current)
            for neighbor in graph[current]:
                if neighbor not in explored:
                    heapq.heappush(frontier, (heuristic(neighbor, goal), path + [neighbor]))
    return None

def heuristic(node, goal): return 0

# Example usage:
graph = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'], 'D': [], 'E': [], 'F': []}
start_node, goal_node = 'A', 'F'
path = best_first_search(graph, start_node, goal_node)
if path:
    print("Path from", start_node, "to", goal_node, ":", path)
else:
    print("No path found from", start_node, "to", goal_node)
