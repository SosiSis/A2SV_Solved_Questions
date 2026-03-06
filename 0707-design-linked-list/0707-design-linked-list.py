class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None


class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        current = self.head.next
        for _ in range(index):
            current = current.next

        return current.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0,val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size,val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return

        prev = self.head
        for _ in range(index):
            prev = prev.next

        newNode = ListNode(val)

        newNode.next = prev.next
        newNode.prev = prev
        prev.next.prev = newNode
        prev.next = newNode

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        prev = self.head
        for _ in range(index):
            prev = prev.next

        prev.next = prev.next.next
        prev.next.prev = prev

        self.size -= 1