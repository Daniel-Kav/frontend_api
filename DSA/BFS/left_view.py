# class Solution:
#     def get_left_view(self, root):
#         if not root:
#             return []
#         #initialize queue as a root and level of search tuple
#         queue = [(root, 0)]
#         result = []
#         max_level = -1 #max level of search tuple

#         while queue:
#             node, level = queue.pop(0)
#                 #if we encounter a new level of search the first node will be added to left_view
#             if level > max_level:
#                 result.append(node.data)
#                 max_level = level

#                 if node.left:
#                     queue.append((node.left, level+ 1))
#                 if node.right:
#                     queue.append((node.right, level+ 1))
#         return result
    

# class Solution :
#     def get_left_view(self, root):
#         if not root:
#             return []
        
#         queue =[(root, 0)]
#         max_level = -1
#         left_view = []

#         while queue:
#             node, level = queue.pop(0)

#             if level > max_level:
#                 left_view.append(node.data)
#                 max_level = level
#             if node.left:
#                 queue.append((node.left, level + 1))
#             if node.right:
#                 queue.append((node.right, level + 1))
#         return left_view

class Solution:
    def get_left_view(self, root):
        if not root:
            return []
        queue =[(root, 0)]
        max_level = -1
        result = []

        while queue:
            node, level = queue.pop(0)

            if level > max_level:
                result.append(node.data)
                max_level = level
            if node.left:
                queue.append((node.left, level +1))
            if node.right:
                queue.append((node.right, level +1))
        return result


class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# Construct the binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.right = Node(8)

sol = Solution()

# Get the left view of the tree
print(sol.get_left_view(root))
