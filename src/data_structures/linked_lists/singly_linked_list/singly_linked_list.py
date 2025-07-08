from typing import Any


class SinglyLinkedListNode:
    def __init__(self, data: Any):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head: SinglyLinkedListNode = None
        self.tail: SinglyLinkedListNode = None
        self.size = 0
        self.sll_initialized = False
        self.sll_node: SinglyLinkedListNode = None
