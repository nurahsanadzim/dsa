from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def __init__(self) -> None:
        self.counter = 1

    def traverseDFS(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    
        if not root:
            return
        
        print(f'value: {root.val}')
        print(f'left: {root.left.val if root.left else None}')
        print(f'right: {root.right.val if root.right else None}')
        print(f'counter: {self.counter}')
        print('')
        
        self.traverseDFS(root.left)
        self.traverseDFS(root.right)

        self.counter += 1

        return root

    def traverseBFS(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    
        if not root:
            return
        
        count = 1
        queue = deque([root])  # Initialize the queue with the root node
        
        while queue:
            node = queue.popleft()  # Dequeue the front node
            
            print(f'val: {root.val}')
            print(f'left: {root.left.val if root.left else None}')
            print(f'right: {root.right.val if root.right else None}')
            
            if node.left:
                queue.append(node.left)  # Enqueue left child if exists
            if node.right:
                queue.append(node.right)  # Enqueue right child if exists
                

            print(f'counter: {count}')
            print('')
            count += 1

        return root

def insert_level_order(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    
    # Loop through the values and build the tree
    while i < len(values):
        current = queue.popleft()
        
        if i < len(values) and values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1
        
        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1
    
    return root

# values = [4, 2, 7, 1, 3, 5, 9, 6, 10, 11, 23, 43, 32, 34, 30, 42, 47]
values = [4, 2, 7, 1, 3, 5, 9]

# Build the tree
root = insert_level_order(values)

sol = Solution()
print('#### BFS ####')
sol.traverseBFS(root)

print('#### DFS ####')
sol.traverseDFS(root)
