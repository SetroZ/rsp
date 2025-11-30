class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root=None):
        self.root = root
    
    def _find(self, node, value):
        if node is None:
            return None
        if value > node.val:
            return self._find(node.right, value)
        elif value < node.val:
            return self._find(node.left, value)
        else:
            return node

    def find(self, value):
        return self._find(self.root, value)

    def _insert(self, node, value):
        if value < node.val:
            if node.left:
                self._insert(node.left, value)
            else:
                node.left = Node(value)
        else:
            if node.right:
                self._insert(node.right, value)
            else:
                node.right = Node(value)

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _remove(self, node, value):
        if node is None:
            return node
        if value < node.val:
            node.left = self._remove(node.left, value)
        elif value > node.val:
            node.right = self._remove(node.right, value)
        else: # Removal logic
            if node.left is None and node.right is None:
                return None
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            minNode = node.right
            while minNode.left:
                minNode = minNode.left
            node.val = minNode.val
            node.right = self._remove(node.right, minNode.val)
        return node

    def remove(self, value):
        self.root = self._remove(self.root, value)
