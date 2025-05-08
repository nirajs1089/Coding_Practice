from typing import Any, Dict, List


def all_simple_paths(
    graph: Dict[Any, List[Any]],
    start: Any,
    target: Any
) -> List[List[Any]]:
    """
    Enumerate all simple paths (no repeated nodes) from `start` to `target`
    in an unweighted directed graph represented as an adjacency list.

    Args:
        graph: mapping from each node to list of its neighbors
        start: the node to start from
        target: the node to reach

    Returns:
        A list of paths, where each path is a list of nodes [start, ..., target].
    """
    def dfs(current: Any, visited: set, path: List[Any], out: List[List[Any]]):
        # If we've reached the target, record a copy of the current path
        if current == target:
            out.append(path.copy())
            return

        # Otherwise, explore each neighbor that has not yet been visited
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                path.append(neighbor)

                dfs(neighbor, visited, path, out)

                # Backtrack: remove neighbor from path and visited
                path.pop()
                visited.remove(neighbor)

    results: List[List[Any]] = []
    dfs(start, {start}, [start], results)
    return results


# ─────────── Test Cases ───────────

if __name__ == "__main__":
    # Example 1: small directed graph
    graph1 = {
        "A": ["B", "C"],
        "B": ["C", "D"],
        "C": ["E"],
        "D": ["C", "E"],
        "E": []
    }
    # Paths from A to C: A->B->C, A->B->D->C, A->C
    expected1 = [
        ["A", "B", "C"],
        ["A", "B", "D", "C"],
        ["A", "C"]
    ]
    result1 = all_simple_paths(graph1, "A", "C")
    assert set(tuple(p) for p in result1) == set(tuple(p) for p in expected1), f"got {result1}"

    # Example 2: no path exists
    graph2 = {"X": ["Y"], "Y": [], "Z": []}
    result2 = all_simple_paths(graph2, "X", "Z")
    assert result2 == [], f"expected empty, got {result2}"

    # Example 3: start == target
    graph3 = {"A": ["B"], "B": ["A"]}
    result3 = all_simple_paths(graph3, "A", "A")
    # One trivial path: ["A"]
    assert result3 == [["A"]], f"expected [['A']], got {result3}"

    # Example 4: undirected graph represented as bidirectional edges
    graph4 = {
        1: [2, 3],
        2: [1, 4],
        3: [1, 4],
        4: [2, 3]
    }
    # Paths from 1 to 4: 1-2-4 and 1-3-4
    expected4 = [
        [1, 2, 4],
        [1, 3, 4]
    ]
    result4 = all_simple_paths(graph4, 1, 4)
    assert set(tuple(p) for p in result4) == set(tuple(p) for p in expected4), f"got {result4}"

    print("All tests passed!")```

**Explanation of the code**  
1. **DFS with backtracking**  
   - We keep a `visited` set to avoid cycles or revisiting a node in the same path.  
   - `path` holds the current sequence of nodes; when we reach `target`, we append a copy of `path` to results.  
   - After exploring a branch, we “backtrack” by popping the last node and removing it from `visited`.  
2. **Edge cases**  
   - If `start == target`, the DFS immediately records the trivial path `[start]`.  
   - If there is no route, we return an empty list.  
3. **Test cases** cover directed, undirected (via bidirectional edges), no-path, and same-node scenarios.
