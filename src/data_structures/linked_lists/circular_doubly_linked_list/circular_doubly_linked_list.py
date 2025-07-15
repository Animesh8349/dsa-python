from typing import Any, Optional


class CircularDoublyLinkedListNode:
    def __init__(self, data: Any):
        self.data = data
        self.next: Optional[CircularDoublyLinkedListNode] = None
        self.prev: Optional[CircularDoublyLinkedListNode] = None


class CircularDoublyLinkedList:
    def __init__(self):
        self.head: Optional[CircularDoublyLinkedListNode] = None
        self.tail: Optional[CircularDoublyLinkedListNode] = None
        self.size = 0
        self.cdll_initialized = False
