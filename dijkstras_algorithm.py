# Dijkstra's algorithm is an algorithm for finding the shortest paths between nodes in graph.
# Works only on not negative edged graph

graph = {}
costs = {}
parents = {}
processed = []

def find_lowest_cost_node(costs):
    lowest_cost = foat('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node 
    

node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors:
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)
