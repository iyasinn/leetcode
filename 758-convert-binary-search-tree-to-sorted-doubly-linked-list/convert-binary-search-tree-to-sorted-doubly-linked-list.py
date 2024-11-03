

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None: 
            return None

        head = None
        prev = None

        def dfs(root):
            nonlocal head
            nonlocal prev
            if root is None: 
                return None, None

            
            dfs(root.left)

            if head:
                root.left = prev
                prev.right = root 
            else:
                head = root
            
            prev = root
            dfs(root.right)

        dfs(root)
        head.left = prev
        prev.right = head
        return head

# class Solution:
#     def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
#         if root is None: 
#             return None

#         eulerPath = []

#         def dfs(root):
#             nonlocal eulerPath
#             if root is None: 
#                 return

#             dfs(root.left)
#             eulerPath.append(root)
#             dfs(root.right)
        
#         dfs(root)

#         head = eulerPath[0]
#         for i, node in enumerate(eulerPath):
#             nextNode = eulerPath[i + 1] if i + 1 < len(eulerPath) else eulerPath[0]
#             prevNode = eulerPath[i - 1] if i - 1 >= 0 else eulerPath[-1]

#             node.left = prevNode
#             node.right = nextNode

        return head






        
        