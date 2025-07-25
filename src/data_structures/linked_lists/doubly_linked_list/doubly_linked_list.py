from typing import Any, Optional


class DoublyLinkedList:
    def __init__(self):
        self.head: Optional[DoublyLinkedListNode] = None
        self.tail: Optional[DoublyLinkedListNode] = None
        self.size = 0
        self.dll_initialized = False
        self.dll_node: Optional[DoublyLinkedListNode] = None


class DoublyLinkedListNode:
    def __init__(self, data: Any):
        self.data = data
        self.next: Optional[DoublyLinkedListNode] = None
        self.prev: Optional[DoublyLinkedListNode] = None

