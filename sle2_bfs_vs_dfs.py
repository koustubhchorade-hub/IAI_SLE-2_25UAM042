from collections import deque
import sys
import networkx as nx
import matplotlib.pyplot as plt


# ==========================================================
# 1. CREATE BINARY TREE
# ==========================================================

def create_tree(depth):

    tree = {}

    # Total nodes = 2^(depth+1) - 1
    total_nodes = (2 ** (depth + 1)) - 1

    for node in range(1, total_nodes + 1):

        left = 2 * node
        right = 2 * node + 1

        children = []

        if left <= total_nodes:
            children.append(left)

        if right <= total_nodes:
            children.append(right)

        if children:
            tree[node] = children

    return tree, total_nodes


# ==========================================================
# 2. DISPLAY TREE
# ==========================================================

def display_tree(tree, depth_to_display=5):

    print("\nTREE STRUCTURE")
    print("=" * 50)

    current_level = [1]

    for level in range(depth_to_display + 1):

        print(f"Level {level}: ", end="")

        for node in current_level:
            print(node, end=" ")

        print()

        next_level = []

        for node in current_level:

            if node in tree:
                next_level.extend(tree[node])

        current_level = next_level


# ==========================================================
# 3. BFS
# ==========================================================

def bfs(tree, start, goal):

    queue = deque([start])
    visited = set()

    nodes_expanded = 0

    while queue:

        current = queue.popleft()

        if current in visited:
            continue

        visited.add(current)
        nodes_expanded += 1

        if current == goal:
            return True, nodes_expanded

        for child in tree.get(current, []):

            if child not in visited:
                queue.append(child)

    return False, nodes_expanded


# ==========================================================
# 4. DFS
# ==========================================================

def dfs(tree, start, goal):

    stack = [start]
    visited = set()

    nodes_expanded = 0

    while stack:

        current = stack.pop()

        if current in visited:
            continue

        visited.add(current)
        nodes_expanded += 1

        if current == goal:
            return True, nodes_expanded

        # Reverse so left child is explored first
        for child in reversed(tree.get(current, [])):

            if child not in visited:
                stack.append(child)

    return False, nodes_expanded


# ==========================================================
# 5. BFS PROFILING WORKLOAD
# ==========================================================

def profile_bfs(tree, start, goal, runs=1000):

    result = None

    for _ in range(runs):
        result = bfs(tree, start, goal)

    return result


# ==========================================================
# 6. DFS PROFILING WORKLOAD
# ==========================================================

def profile_dfs(tree, start, goal, runs=1000):

    result = None

    for _ in range(runs):
        result = dfs(tree, start, goal)

    return result


# ==========================================================
# 7. VISUALIZE GRAPH
# ==========================================================

def visualize_graph(tree, bfs_path=None):

    # Display first 31 nodes
    display_nodes = 31

    G = nx.DiGraph()

    for node in range(1, display_nodes + 1):

        for child in tree.get(node, []):

            if child <= display_nodes:
                G.add_edge(node, child)

    # Create tree layout
    pos = {}

    levels = 5

    for level in range(levels + 1):

        start_node = 2 ** level
        end_node = (2 ** (level + 1)) - 1

        nodes_at_level = end_node - start_node + 1

        for j, node in enumerate(
            range(start_node, end_node + 1)
        ):

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

    # Highlight BFS path if supplied
    if bfs_path:

        bfs_edges = list(
            zip(bfs_path[:-1], bfs_path[1:])
        )

        visible_edges = [
            edge
            for edge in bfs_edges
            if edge[0] <= display_nodes
            and edge[1] <= display_nodes
        ]

        nx.draw_networkx_edges(
            G,
            pos,
            edgelist=visible_edges,
            width=3
        )

    plt.title(
        "Binary Tree Graph Used for BFS and DFS\n"
        "(First 31 nodes shown)"
    )

    plt.axis("off")

    plt.show()


# ==========================================================
# 8. MAIN PROGRAM
# ==========================================================

def main():

    START = 1

    # Depth 15 = 65,535 nodes
    TREE_DEPTH = 15

    PROFILE_RUNS = 1000

    # Create tree
    tree, total_nodes = create_tree(TREE_DEPTH)

    print("=" * 60)
    print("          BFS vs DFS SEARCH PROFILING")
    print("=" * 60)

    print(f"\nTotal nodes in tree : {total_nodes}")
    print(f"Tree depth          : {TREE_DEPTH}")

    display_tree(tree, depth_to_display=5)

    print("\n...")
    print(f"... tree continues up to {total_nodes}")
    print()

    # ------------------------------------------------------
    # Check command-line mode
    # ------------------------------------------------------

    if len(sys.argv) > 1:

        mode = sys.argv[1].lower()

        # --------------------------------------------------
        # BFS PROFILING MODE
        # --------------------------------------------------

        if mode == "bfs":

            GOAL = 15000

            print("\nBFS PROFILING MODE")
            print("=" * 60)

            print(f"Start node : {START}")
            print(f"Goal node  : {GOAL}")
            print(f"Runs       : {PROFILE_RUNS}")

            profile_bfs(
                tree,
                START,
                GOAL,
                PROFILE_RUNS
            )

            print("\nBFS profiling workload completed.")

            return

        # --------------------------------------------------
        # DFS PROFILING MODE
        # --------------------------------------------------

        elif mode == "dfs":

            GOAL = 15000

            print("\nDFS PROFILING MODE")
            print("=" * 60)

            print(f"Start node : {START}")
            print(f"Goal node  : {GOAL}")
            print(f"Runs       : {PROFILE_RUNS}")

            profile_dfs(
                tree,
                START,
                GOAL,
                PROFILE_RUNS
            )

            print("\nDFS profiling workload completed.")

            return

    # ======================================================
    # NORMAL MODE
    # ======================================================

    while True:

        try:

            goal = int(
                input(
                    "Enter the number you want to search: "
                )
            )

            if 1 <= goal <= total_nodes:
                break

            print(
                f"Please enter a number between 1 and "
                f"{total_nodes}."
            )

        except ValueError:

            print("Please enter a valid integer.")

    print("\n" + "=" * 60)
    print("SEARCH REQUEST")
    print("=" * 60)

    print(f"Starting node : {START}")
    print(f"Searching for : {goal}")

    # ------------------------------------------------------
    # BFS
    # ------------------------------------------------------

    bfs_found, bfs_nodes = bfs(
        tree,
        START,
        goal
    )

    # ------------------------------------------------------
    # DFS
    # ------------------------------------------------------

    dfs_found, dfs_nodes = dfs(
        tree,
        START,
        goal
    )

    # ------------------------------------------------------
    # Results
    # ------------------------------------------------------

    print("\n" + "=" * 60)
    print("                 RESULTS")
    print("=" * 60)

    print("\nBREADTH FIRST SEARCH (BFS)")
    print("-" * 40)

    print(f"Target             : {goal}")
    print(f"Found              : {bfs_found}")
    print(f"Nodes Expanded     : {bfs_nodes}")

    print("\nDEPTH FIRST SEARCH (DFS)")
    print("-" * 40)

    print(f"Target             : {goal}")
    print(f"Found              : {dfs_found}")
    print(f"Nodes Expanded     : {dfs_nodes}")

    print("\n" + "=" * 60)
    print("             PROFILING COMMANDS")
    print("=" * 60)

    print("\nBFS terminal profiling:")
    print("py-spy top -- python sle2_bfs_vs_dfs.py bfs")

    print("\nDFS terminal profiling:")
    print("py-spy top -- python sle2_bfs_vs_dfs.py dfs")

    print("\nBFS flame graph:")
    print(
        "py-spy record -o bfs_flamegraph.svg "
        "-- python sle2_bfs_vs_dfs.py bfs"
    )

    print("\nDFS flame graph:")
    print(
        "py-spy record -o dfs_flamegraph.svg "
        "-- python sle2_bfs_vs_dfs.py dfs"
    )

    print("=" * 60)

    # ------------------------------------------------------
    # Visualize graph
    # ------------------------------------------------------

    visualize_graph(tree)


# ==========================================================
# 9. PROGRAM START
# ==========================================================

if __name__ == "__main__":
    main()
