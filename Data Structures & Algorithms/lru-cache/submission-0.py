class Node:
    def __init__(self, key: int, value: int, next=None, prev=None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)

        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        curr = self.removeNode(self.cache[key])
        curr = self.addNode(curr, self.tail)

        return curr.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].value = value
            curr = self.removeNode(self.cache[key])
            curr = self.addNode(curr, self.tail)
            return
        
        node = Node(key, value)
        self.addNode(node, self.tail)
        self.cache[key] = node
        self.size += 1

        if self.size > self.capacity:
            removed = self.removeNode(self.head.next)
            del self.cache[removed.key]
            self.size -= 1

        

    def removeNode(self, node: Node) -> Node:
        if not node:
            return None

        prevNode = node.prev
        nextNode = node.next

        nextNode.prev = prevNode
        prevNode.next = nextNode

        node.prev = None
        node.next = None

        return node
    
    def addNode(self, node: Node, tail: Node) -> Node:
        temp = tail.prev

        node.prev = temp
        node.next = tail

        temp.next = node
        tail.prev = node
        return node
