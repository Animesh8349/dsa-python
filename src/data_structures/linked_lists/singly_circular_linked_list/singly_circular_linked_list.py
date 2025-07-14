from typing import Any, Optional


class SinglyCircularLinkedListNode:
    def __init__(self, data: Any):
        self.data = data
        self.next: Optional[SinglyCircularLinkedListNode] = None


class SinglyCircularLinkedList:
    def __init__(self):
        self.head: Optional[SinglyCircularLinkedListNode] = None
        self.tail: Optional[SinglyCircularLinkedListNode] = None
        self.size = 0
        self.sll_initialized = False
