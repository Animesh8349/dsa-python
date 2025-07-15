from typing import Any, Optional


class CircularSinglyLinkedListNode:
    def __init__(self, data: Any):
        self.data = data
        self.next: Optional[CircularSinglyLinkedListNode] = None


class CircularSinglyLinkedList:
    def __init__(self):
        self.head: Optional[CircularSinglyLinkedListNode] = None
        self.tail: Optional[CircularSinglyLinkedListNode] = None
        self.size = 0
        self.csll_initialized = False
