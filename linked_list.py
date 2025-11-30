
    
class LL:
    class Node:
        def __init__(self):
            self.next = None
            self.val = None

    def __init__(self):
        self.head = None
        self.tail = None
    def addNode(self,val):
        node = self.Node()
        node.val = val
        if not self.head:
            self.head = node
            self.tail = node
        elif self.tail:
            self.tail.next = node
            self.tail = node
    def removeNode(self,val):
        prev = None
        curr = self.head
        while curr:
            if curr.val == val:
                if curr == self.head:
                    self.head = self.head.next
                if curr == self.tail:
                    self.tail = prev
                    if self.tail:
                        self.tail.next = None
                if prev:
                    prev.next = curr.next
                return
            prev = curr
            curr = curr.next

ll = LL()

# Add nodes
ll.addNode(1)
ll.addNode(2)
ll.addNode(3)


curr = ll.head
print("List after adding 1,2,3:")
while curr:
    print(curr.val, end=" ")
    curr = curr.next
print()
print("head:", ll.head.val)
print("tail:", ll.tail.val)

ll.removeNode(2)
curr = ll.head
print("List after removing 2:")
while curr:
    print(curr.val, end=" ")
    curr = curr.next
print()
print("head:", ll.head.val)
print("tail:", ll.tail.val)

ll.removeNode(1)
curr = ll.head
print("List after removing 1:")
while curr:
    print(curr.val, end=" ")
    curr = curr.next
print()
print("head:", ll.head.val)
print("tail:", ll.tail.val)

ll.removeNode(3)
curr = ll.head
print("List after removing 3")
while curr:
    print(curr.val, end=" ")
    curr = curr.next





