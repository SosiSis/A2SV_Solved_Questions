class MyCircularDeque:

    def __init__(self, k: int):
        self.my_deque = []
        self.size = k

    def insertFront(self, value: int) -> bool:
        if len(self.my_deque) == self.size:
            return False
        self.my_deque.insert(0, value)
        return True

    def insertLast(self, value: int) -> bool:
        if len(self.my_deque) == self.size:
            return False
        self.my_deque.append(value)
        return True

    def deleteFront(self) -> bool:
        if not self.my_deque:
            return False
        self.my_deque.pop(0)
        return True

    def deleteLast(self) -> bool:
        if not self.my_deque:
            return False
        self.my_deque.pop()
        return True

    def getFront(self) -> int:
        if not self.my_deque:
            return -1
        return self.my_deque[0]

    def getRear(self) -> int:
        if not self.my_deque:
            return -1
        return self.my_deque[-1]

    def isEmpty(self) -> bool:
        return len(self.my_deque) == 0

    def isFull(self) -> bool:
        return len(self.my_deque) == self.size