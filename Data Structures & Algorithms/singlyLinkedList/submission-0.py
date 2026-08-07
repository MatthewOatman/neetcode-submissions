class Node:
    def __init__(self, val):
        self.next = None
        self.value = val

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.length = 0

    def get(self, index: int) -> int:
        if index in range(self.length):
            node = self.head
            for i in range(index):
                node = node.next

            return node.value
        else:
            return -1


    def insertHead(self, val: int) -> None:
        self.length += 1

        newHead = Node(val)
        newHead.next = self.head
        self.head = newHead

    def insertTail(self, val: int) -> None:
        self.length += 1

        if self.head == None:
            self.head = Node(val)
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = Node(val)

    def remove(self, index: int) -> bool:
        if index in range(self.length):
            self.length -= 1

            # Edge case when removing head
            if index == 0:
                self.head = self.head.next
            else:
                # Iterate until the previous before the index
                prev = self.head
                for i in range(index - 1):
                    prev = prev.next
                
                prev.next = prev.next.next

            return True
        else:
            return False


    def getValues(self) -> List[int]:
        res = []

        node = self.head
        while node:
            res.append(node.value)
            node = node.next

        return res
