from collections import deque
from typing import Any, Dict, List, Optional

def shortest_path_bfs(
    graph: Dict[Any, List[Any]],
    start: Any,
    target: Any
) -> Optional[List[Any]]:
    """
    Find the shortest path between `start` and `target` in an unweighted graph
    using breadth-first search (BFS). Returns the list of nodes from start to
    target, or None if no path exists.

    Args:
        graph: A mapping from each node to a list of its neighbors.
        start: The node where the search begins.
        target: The node we want to reach.

    Returns:
        A list of nodes representing the shortest path from start to target,
        inclusive, or None if the target is not reachable.
    """
    # Edge case: start and target are the same
    if start == target:
        return [start]

    # Queue for BFS, initialized with the start node
    queue = deque([start])
    # Keep track of visited nodes to avoid revisiting
    visited = {start}
    # Parent map to reconstruct the path at the end:
    # parent[node] = the node we came from when we first visited `node`
    parent: Dict[Any, Any] = {}

    # Perform BFS
    while queue:
        current = queue.popleft()
        # Explore each neighbor of the current node
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)

                # Stop early if we've reached the target
                if neighbor == target:
                    # Reconstruct the path by walking backwards through parents
                    path = [target]
                    while path[-1] != start:
                        path.append(parent[path[-1]])
                    path.reverse()
                    return path

    # If we exit the loop without finding the target, no path exists
    return None


# ───────── Example Usage ─────────

if __name__ == "__main__":
    # Define a simple unweighted graph as an adjacency list
    example_graph = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"]
    }

    path = shortest_path_bfs(example_graph, start="A", target="F")
    print(path)  # Output should be ['A', 'C', 'F']
