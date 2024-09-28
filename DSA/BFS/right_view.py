class Solution:
    def right_view(self,root):
        if root is None: return []

        queue = []
        queue.append(root)
        result = []
        height = 0

        while queue:
            count = len(queue)
            height += 1
            for i in range(count):
                node = queue.pop(0)

                if i == 0:
                    result.append(node.data) # append the last node which is ussually the right node to the right view
                if node.left :
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result, height



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
print("Right view of the binary tree is:", sol.right_view(root))

