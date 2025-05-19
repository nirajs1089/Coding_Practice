 def solveTree(self, root: TreeNode) -> int:
        """
        Replace `solveTree` with the LeetCode function name (e.g. maxDepth, diameterOfBinaryTree, etc.)
        Return type (`int` here) should match the problem’s requirement.
        """

        # Edge case: empty tree
        if not root:
            return 0  # or appropriate default ([], None, "", etc.)

        # ------------------------------
        # 1. Recursive DFS helper
        # ------------------------------
        # Example pattern: returns some value per subtree and optionally updates self.result
        # Uncomment and adapt this block if a post-order recursion fits the problem.

        self.result = INITIAL_VALUE  # e.g. 0, float('-inf'), []
        visited = set()

        def dfs(node: TreeNode, count) -> int:
            if not node and node not in visited:
                return BASE_VALUE  # e.g. 0 for depths, 1 for counts

            visited.add(node)  # to avoid duplicate node processing and avoid cycles in tree
            # Recurse left and right
            left_val = dfs(node.left,INITIAL_VALUE + INCREMENT)  #compound addition
            right_val = dfs(node.right,INITIAL_VALUE + INCREMENT)

            # Combine: update global result if needed
            # self.result = max(self.result, left_val + right_val + EXTRA)

            # Return value upward
            return RETURN_EXPRESSION  # e.g. 1 + max(left_val, right_val)

        dfs(root)
        return self.result

        # ------------------------------
        # 2. Iterative DFS (stack) template
        # ------------------------------
        # Use when recursion might overflow or you need explicit state.
        #
        stack = [(root, STATE_INITIAL, None)]  
        # STATE_INITIAL: indicates we need to visit children first
        # You can push (node, STATE_AFTER, left_val, right_val) to track post-order

        while stack:
            node, state, data = stack.pop()
            if not node:
                continue

            if state == STATE_INITIAL:
                # Post-order: push work after children
                stack.append((node, STATE_AFTER, None))
                # Push children to be processed first
                # modify the children before pushing on to stack
                stack.append((node.right + node.data, STATE_INITIAL, None))
                stack.append((node.right, STATE_INITIAL, None))
                stack.append((node.left, STATE_INITIAL, None))
                stack.append((parent[node], STATE_INITIAL, None)) #if parent dict is created then use parent as 3rd child to traverse in all directions
            else:
                # STATE_AFTER: children done, compute using data collected
                # left_val, right_val = data
                # update result or transform node
                pass

        return FINAL_RESULT

        # ------------------------------
        # 3. BFS / Level-Order template
        # ------------------------------
        # Use when you need the tree by levels or shortest distance in unweighted tree.
        #
        from collections import deque
        queue = deque([root])
        result = []
        while queue:
            level_size = len(queue)
            level = []
            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # process level (e.g. result.append(level), track max width, etc.)
            result.append(level)
        return result  # or derive answer from `result`

        # ------------------------------
        # 4. Common utility snippets
        # ------------------------------

        # Pre-order traversal (root-left-right)
        def preorder(node):
            if not node: return
            # visit node.val
            preorder(node.left)
            preorder(node.right)

        # In-order traversal (left-root-right)
        def inorder(node):
            if not node: return
            inorder(node.left)
            # visit node.val
            inorder(node.right)

        # Post-order traversal (left-right-root)
        def postorder(node):
            if not node: return
            postorder(node.left)
            postorder(node.right)
            # visit node.val

        # ------------------------------
        # 5. Final stub (customize this)
        # ------------------------------
        # If none of the above, write your custom logic here:
        #
        answer = SOME_INITIAL_VALUE
        # e.g., traverse and compute
        return answer

        # Placeholder return; remove once you implement one of the above patterns.
        return -1
