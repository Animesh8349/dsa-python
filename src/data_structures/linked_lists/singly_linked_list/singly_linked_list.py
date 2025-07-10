from typing import Any, Optional


class SinglyLinkedListNode:
    def __init__(self, data: Any):
        self.data = data
        self.next: Optional[SinglyLinkedListNode] = None


class SinglyLinkedList:
    def __init__(self):
        self.head: Optional[SinglyLinkedListNode] = None
        self.tail: Optional[SinglyLinkedListNode] = None
        self.size = 0
        self.sll_initialized = False
        self.sll_node: Optional[SinglyLinkedListNode] = None
