# SLE-2: BFS vs DFS Profiling

**Course:** 02AML204 – Introduction to Artificial Intelligence

**PRN:** 25UAM042

**Name:** Koustubh Sampat Chorade

**Division:** A

## About the Project

This project is part of **SLE-2: Profiling Report** for the Introduction to Artificial Intelligence course.

The project compares the empirical performance of two uninformed search algorithms:

* Breadth-First Search (BFS)
* Depth-First Search (DFS)

Both algorithms are tested on the same binary-tree graph.

## Objective

The main objective is to:

* Implement BFS and DFS in Python.
* Measure their execution time.
* Count the number of nodes expanded.
* Profile their execution using Py-Spy.
* Compare the observed performance of both algorithms.

## Graph Used

The experiment uses a binary-tree graph with:

* **Vertices (V):** 65,535
* **Edges (E):** 65,534
* **Start Node:** 0
* **Goal Node:** 30,000

## Profiling Tools

### 1. timeit

Python's built-in `timeit` module is used to measure the execution time of BFS and DFS.

### 2. Py-Spy

Py-Spy is used to profile the Python program and generate flamegraphs showing where execution time is spent.

### 3. Node Counter

A `nodes_expanded` counter is maintained in both algorithms to record the number of nodes examined before reaching the goal.

## Experimental Results

| Metric         |     BFS |      DFS |
| -------------- | ------: | -------: |
| Average Time   | 5.29 ms | 23.42 ms |
| Nodes Expanded |  15,000 |   54,472 |

The reported values are from the selected experiment documented in the SLE-2 report.

## Complexity

| Algorithm | Best Case | Average Case | Worst Case | Space Complexity |
| --------- | --------- | ------------ | ---------- | ---------------- |
| BFS       | O(1)      | O(V)         | O(V)       | O(V)             |
| DFS       | O(1)      | O(V)         | O(V)       | O(V)             |

Where **V** represents the number of vertices.

## Analysis

For this particular experiment, BFS had a lower measured execution time and expanded fewer nodes than DFS.

BFS took **5.29 ms** and expanded **15,000 nodes**, while DFS took **23.42 ms** and expanded **54,472 nodes**.

Therefore, based on the measured results, BFS showed better performance for this specific graph and goal node. The result is specific to the selected graph, implementation, and test conditions.

## Flamegraphs

The `profiling` folder contains the flamegraphs generated during profiling:

* `bfs_flamegraph.svg`
* `dfs_flamegraph.svg`

These provide a visual representation of the program's execution during profiling.

## Repository Structure

```text
IAI_SLE-2_25UAM042/
│
├── README.md
├── bfs_dfs_profiling.py
├── AI_Contribution_Log.md
│
├── profiling/
│   ├── bfs_flamegraph.svg
│   └── dfs_flamegraph.svg
│
└── report/
    └── SLE2_25UAM042_Koustubh_Sampat_Chorade.pdf
```

## AI Contribution

ChatGPT was used to:

* Understand BFS and DFS concepts.
* Assist with the Python implementation structure.
* Understand profiling using `timeit` and Py-Spy.
* Help interpret the experimental results.
* Assist in preparing the SLE-2 documentation.

The final program was executed and tested by the student, and the reported performance values were obtained from the student's execution.

## Conclusion

This project demonstrates the empirical performance comparison of BFS and DFS on the same binary-tree graph.

The experiment shows that execution time and the number of nodes expanded are useful measures for analysing search algorithms. Profiling helps observe the actual behaviour of an implementation under specific test conditions.
