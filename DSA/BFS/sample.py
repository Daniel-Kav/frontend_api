# # class Node:
# #     def __init__(self, key):
# #         self.data = key
# #         self.left = None
# #         self.right = None

# # def printLevelOrder(root):

# #     if root is None:
# #         return
    
# #     queue = []

# #     queue.append(root)
    
# #     while queue:
            
# #         node = queue.pop(0)
# #         print(node.data, end=" ")

# #         if node.left is not None:
# #             queue.append(node.left)
        
# #         if node.right is not None:
# #             queue.append(node.right)

# # if __name__ == "__main__":
# #     root = Node(1)
# #     root.left = Node(2)
# #     root.right = Node(3)
# #     root.left.left = Node(4)
# #     root.left.right = Node(5)
# #     printLevelOrder(root)

# class Node:
#     def __init__(self, key):
#         self.data = key
#         self.right = None
#         self.left = None

# def BFS(root):
#     #chek for root node
#     if root is None: return
#     #initialize a queue
#     queue = []
#     #enqueue the root node
#     queue.append(root)

#     #iterate over the nodes to find the height
#     while queue:
#         #pop the node off the queue and print it
#         node = queue.pop(0)
#         print(node.data, end=" ")

#         #enqueue the left child
#         if node.left is not None:
#             queue.append(node.left)

#         if node.right is not None:
#             queue.append(node.right)


# if __name__ == "__main__":
#     root = Node(6)
#     root.left = Node(7)
#     root.right = Node(8)
#     root.left.left = Node(9)
#     root.right.left = Node(10)
#     root.right.right = Node(11)
#     BFS(root)

class Solution:
    def BFS(self, root):
        if not root:
            return
        queue = []
        result = []
        queue.append(root)

        while queue:
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result



class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

# Construct the binary tree as given in the problem
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.right = Node(8)

sol = Solution()
print("Right view of the binary tree is:", sol.BFS(root))
