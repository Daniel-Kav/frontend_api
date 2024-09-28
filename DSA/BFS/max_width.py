# class Solution:

# # func
#     def max_width(self, root):
#         if root is None: return 0
#         # initialize queue append root and initial max_width of the tree
#         queue = []
#         queue.append(root)
#         max_width = 0

#         # level order traversal
#         while queue:
#             # number of nodes at the current level
#             count = len(queue)

#             # update max_width
#             max_width = max(max_width, count)
#             # process all nodes at the current level
#             for _ in range(count):
#                 node = queue.pop(0)# deque node

#                     # enqueue left child
#                 if node.left is not None:
#                     queue.append(node.left)

#                 # enqueue right child if exists
#                 if node.right is not None:
#                     queue.append(node.right)

#         # return max width
#         return max_width

class Solution:
    def get_max_width(self, root):
        if root is  None:
            return 0
        
        queue = []
        queue.append(root)
        max_width =0

        while queue:
            count = len(queue)
            max_width = max(max_width,count)

            for _ in range(count):
                node = queue.pop(0)

                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
        return max_width


class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

# Construct a binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
root.left.left.left = Node(7)

# Create an object of the Solution class
sol = Solution()

# Get the maximum width of the tree
print("Maximum width of the binary tree is:", sol.get_max_width(root))