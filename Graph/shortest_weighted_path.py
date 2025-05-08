from typing import Any, Dict, List, Tuple, Optional
import heapq

def dijkstra_shortest_path(
    graph: Dict[Any, List[Tuple[Any, float]]],
    start: Any,
    target: Any
) -> Tuple[Optional[float], List[Any]]:
    """
    Find the shortest path and its distance from start to target in a graph
    with positive edge weights using Dijkstra's algorithm.
    
    Args:
        graph: A mapping where graph[u] is a list of (v, weight) edges.
        start: The source node.
        target: The destination node.
    
    Returns:
        A tuple (distance, path):
          - distance: the total weight of the shortest path (None if unreachable)
          - path: the list of nodes from start to target (empty if unreachable)
    """
    # Min-heap of (current_distance, node)
    heap: List[Tuple[float, Any]] = [(0.0, start)]
    
    # Distance from start to each node; default to infinity
    distances: Dict[Any, float] = {start: 0.0}
    
    # Parent map for path reconstruction
    parent: Dict[Any, Any] = {}
    
    while heap:
        curr_dist, node = heapq.heappop(heap)
        
        # If we reached target, we can stop
        if node == target:
            break
        
        # If this heap entry is stale, skip it
        if curr_dist > distances.get(node, float('inf')):
            continue
        
        # Relaxation step
        for neighbor, weight in graph.get(node, []):
            new_dist = curr_dist + weight
            # If found shorter path to neighbor
            if new_dist < distances.get(neighbor, float('inf')):
                distances[neighbor] = new_dist
                parent[neighbor] = node
                heapq.heappush(heap, (new_dist, neighbor))
    
    # If target is unreachable
    if target not in distances:
        return None, []
    
    # Reconstruct path from target to start
    path: List[Any] = []
    node = target
    while node != start:
        path.append(node)
        node = parent[node]
    path.append(start)
    path.reverse()
    
    return distances[target], path

# ─────────── Test Cases ───────────

if __name__ == "__main__":
    # Example graph
    graph1 = {
        'A': [('B', 1), ('C', 4)],
        'B': [('C', 2), ('D', 5)],
        'C': [('D', 1)],
        'D': []
    }
    dist1, path1 = dijkstra_shortest_path(graph1, 'A', 'D')
    assert dist1 == 4.0, f"Expected distance 4.0, got {dist1}"
    assert path1 == ['A', 'B', 'C', 'D'], f"Expected path ['A','B','C','D'], got {path1}"

    # Start equals target
    dist2, path2 = dijkstra_shortest_path(graph1, 'A', 'A')
    assert dist2 == 0.0, f"Expected distance 0.0, got {dist2}"
    assert path2 == ['A'], f"Expected path ['A'], got {path2}"

    # No path available
    graph2 = {'X': [('Y', 3)], 'Y': [], 'Z': []}
    dist3, path3 = dijkstra_shortest_path(graph2, 'X', 'Z')
    assert dist3 is None and path3 == [], f"Expected (None, []), got ({dist3}, {path3})"

    print("All tests passed!")
