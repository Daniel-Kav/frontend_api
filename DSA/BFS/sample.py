class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def printLevelOrder(root):

    if root is None:
        return
    
    queue = []

    queue.append(root)
    
    while queue:
            
        node = queue.pop(0)
        print(node.data, end=" ")

        if node.left is not None:
            queue.append(node.left)
        
        if node.right is not None:
            queue.append(node.right)

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    printLevelOrder(root)