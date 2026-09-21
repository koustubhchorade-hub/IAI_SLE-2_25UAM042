import timeit
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt


# Generate a binary tree graph
graph = {}

number_of_nodes = 16383

for i in range(number_of_nodes):
    children = []

    left = 2 * i + 1
    right = 2 * i + 2

    if left < number_of_nodes:
        children.append(left)

    if right < number_of_nodes:
        children.append(right)

    graph[i] = children


# ---------------- BFS ----------------
def bfs(graph, start, goal):
    queue = deque([start])
    visited = set([start])
    parent = {start: None}
    nodes_expanded = 0

    while queue:
        current = queue.popleft()
        nodes_expanded += 1

        if current == goal:
            # Reconstruct path
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]

            return nodes_expanded, path[::-1]

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)

    return nodes_expanded, []


# ---------------- DFS ----------------
def dfs(graph, start, goal):
    stack = [start]
    visited = set([start])
    parent = {start: None}
    nodes_expanded = 0

    while stack:
        current = stack.pop()
        nodes_expanded += 1

        if current == goal:
            # Reconstruct path
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]

            return nodes_expanded, path[::-1]

        for neighbor in reversed(graph[current]):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                stack.append(neighbor)

    return nodes_expanded, []


# ---------------- Start and Goal ----------------
start = 0
goal = 15000


# Run BFS and DFS
bfs_nodes, bfs_path = bfs(graph, start, goal)
dfs_nodes, dfs_path = dfs(graph, start, goal)


# ---------------- Measure Execution Time ----------------
number_of_runs = 100

bfs_time = timeit.timeit(
    lambda: bfs(graph, start, goal),
    number=number_of_runs
)

dfs_time = timeit.timeit(
    lambda: dfs(graph, start, goal),
    number=number_of_runs
)


# Average time in milliseconds
bfs_average = (bfs_time / number_of_runs) * 1000
dfs_average = (dfs_time / number_of_runs) * 1000


# ---------------- Display Results ----------------
print("========== RESULTS ==========")

print("BFS nodes expanded:", bfs_nodes)
print("DFS nodes expanded:", dfs_nodes)

print("BFS average time:", bfs_average, "ms")
print("DFS average time:", dfs_average, "ms")

print("\nBFS Path:")
print(bfs_path)

print("\nDFS Path:")
print(dfs_path)


# =========================================================
# VISUALIZE THE ACTUAL GRAPH
# =========================================================

# Display first 31 nodes of the SAME binary tree
display_nodes = 31

G = nx.DiGraph()

for node in range(display_nodes):
    for child in graph[node]:
        if child < display_nodes:
            G.add_edge(node, child)


# Create tree layout manually
pos = {}

levels = 5

for level in range(levels):
    start_node = 2**level - 1
    end_node = 2**(level + 1) - 2

    nodes_at_level = end_node - start_node + 1

    for j, node in enumerate(range(start_node, end_node + 1)):
        x = (j + 1) / (nodes_at_level + 1)
        y = -level
        pos[node] = (x, y)


# Draw graph
plt.figure(figsize=(14, 8))

nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=900,
    font_size=9,
    arrows=True
)


# Highlight BFS path
bfs_edges = list(zip(bfs_path[:-1], bfs_path[1:]))

# Only highlight edges visible in displayed graph
bfs_edges_display = [
    edge for edge in bfs_edges
    if edge[0] < display_nodes and edge[1] < display_nodes
]

nx.draw_networkx_edges(
    G,
    pos,
    edgelist=bfs_edges_display,
    width=3
)


plt.title(
    "Binary Tree Graph Used for BFS and DFS\n"
    "(First 31 nodes shown from the 16,383-node graph)"
)

plt.axis("off")
plt.show()