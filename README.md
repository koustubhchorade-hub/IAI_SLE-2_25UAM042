# IAI_SLE-2_25UAM042

## SLE-2: BFS vs DFS Performance Profiling

**Course:** 02AML204 – Introduction to Artificial Intelligence  
**PRN:** 25UAM042  
**Name:** Koustubh Sampat Chorade  
**Division:** A  

## About

This project compares the performance of **Breadth First Search (BFS)** and **Depth First Search (DFS)** on a binary-tree graph using Python.

## Objective

- Implement BFS and DFS.
- Measure execution time using Python's `timeit` module.
- Compare execution time and nodes expanded.

## Results

| Metric | BFS | DFS |
|---|---:|---:|
| Average Time | 4.6994 ms | 7.0109 ms |
| Nodes Expanded | 15,001 | 13,625 |

BFS recorded a lower execution time, while DFS expanded fewer nodes in this experiment.

## Technologies Used

- Python
- VS Code
- `timeit`
- GitHub

## Files

- `sle2_bfs_vs_dfs.py` – BFS and DFS implementation
- `AI Contribution log.md` – AI contribution details
- `README.md` – Project documentation

## AI Contribution

ChatGPT was used to understand BFS and DFS, structure the Python implementation, understand `timeit`, and interpret the profiling results. The program was executed and tested by the student, and the reported performance values were obtained from the actual execution.

## Conclusion

The experiment shows that **execution time and number of nodes expanded are separate performance measures**. The results depend on the graph, implementation, and execution environment.
