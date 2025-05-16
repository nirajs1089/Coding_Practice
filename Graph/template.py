from collections import deque


Adjacency list
def number_of_paths(n, corridors):
    neighbours = defaultdict(set)
    cycles = 0


    for room1, room2 in corridors:
        neighbours[room1].add(room2)
        neighbours[room2].add(room1)




class TreeNode:
   def __init__(self, value):
       self.value = value
       self.children = []  # list of TreeNode


# Breadth-First Search (BFS) using a queue
def bfs(root: TreeNode):
   if not root:
       return


   q = deque([root])
   Visited = set()
   while q:
       node = q.popleft()
       # ---- process node here ----


      If node not in visited: 
     print(node.value)
       if node.value == DESTINATION;
  	    print("destination found")


       for child in node.children:
           q.append(child) OR
           q.append(child, weight) OR
           q.append(child, grouping)




# Depth-First Search (DFS) using an explicit stack (iterative preorder)
def dfs_with_stack(root: TreeNode):
   if not root:
       return


   stack = [root]
   while stack:
       node = stack.pop()
       # ---- process node here ----
       print(node.value)
       # Push children in reverse order so that
       # the “first” child is processed first
       for child in reversed(node.children):
           # stack.append(node.val + child)
           stack.append(child)
		if child.value in stack:
   			print("Cycle exists")




# BFS or DFS depending on the lowest weight of the edge (child,sibling)
def combo(root: TreeNode):
   if not root:
       return


   q = heap.add((weight,node))
   while q:
       weight, node = q.pop()
       # ---- process node here ----
       print(node.value)
       if node.value == DESTINATION;
  	    print("destination found")
	
	process_weight


       for child in node.children or :
           q.push(child)
