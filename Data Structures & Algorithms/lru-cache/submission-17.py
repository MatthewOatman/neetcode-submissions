class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.length = 0

        self.leftEnd = Node(0, 0)
        self.rightEnd = Node(0, 0)
        self.leftEnd.next = self.rightEnd
        self.rightEnd.prev = self.leftEnd

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.remove(node)
        self.add(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.remove(node)
            self.add(node)
        else:
            if self.length == self.cap:
                lru = self.leftEnd.next
                self.remove(lru)
                del self.cache[lru.key]
                self.length -= 1

            node = Node(key, value)
            self.cache[key] = node
            self.add(node)
            self.length += 1

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def add(self, node):
        prev = self.rightEnd.prev
        prev.next = node
        node.prev = prev
        node.next = self.rightEnd
        self.rightEnd.prev = node