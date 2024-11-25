from collections import deque

# реализация с помощью deque
class queue:
    def __init__(self):
        self.queue = deque()
    def add(self, x):
        self.queue.append(x)
    def remove(self) -> int:
        # если не пустая
        if self.queue:
            return self.queue.popleft()
        return -1
    def CheckFirst(self) -> int:
        # если не пустая
        if self.queue:
            return self.queue[0]
        return -1

# вершина двусвязанного списка
class LinkedListNode:
    def __init__(self, val = 0, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

#реализация с помощью двусвязанного списка
class queue2:
    def __init__(self):
        self.left = None
        self.right = None
    def add(self, x):
        # если не пустая
        if self.right:
            self.right.next = LinkedListNode(x)
            self.right.next.prev = self.right
            self.right = self.right.next
        # если пустая
        else:
            self.right = LinkedListNode(x)
            self.left = self.right
    def remove(self):
        # если пустая
        if not self.left:
            return -1
        value = self.left.val
        # если всего один элемент
        if self.left == self.right:
            self.left = None
            self.right = None
        # если элементов больше одного
        else:
            self.left = self.left.next
        return value
    def CheckFirst(self):
        # если пустая
        if not self.left:
            return -1
        return self.left.val