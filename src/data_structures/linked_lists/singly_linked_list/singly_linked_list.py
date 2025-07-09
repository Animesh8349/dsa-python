from typing import Any, Optional


class SinglyLinkedList:
    def __init__(self):
        self.head: Optional[SinglyLinkedListNode] = None
        self.tail: Optional[SinglyLinkedListNode] = None
        self.size = 0
        self.sll_initialized = False
        self.sll_node: Optional[SinglyLinkedListNode] = None


class SinglyLinkedListNode:
    def __init__(self, data: Any):
        self.data = data
        self.next: Optional[SinglyLinkedListNode] = None


class MultipleElementsHandler:
    def __init__(self, index, element):
        self.index = index
        self.element = element


def sort_list_multiple_elements_handlers(
    multiple_elements_handler_list: list[MultipleElementsHandler],
) -> list[MultipleElementsHandler]:
    return sorted(multiple_elements_handler_list, key=lambda k: k.index)
