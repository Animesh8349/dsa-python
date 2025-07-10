"""
Unit tests for the SinglyLinkedList class.
"""

import pytest
from src.data_structures.linked_lists.singly_linked_list.singly_linked_list import (
    SinglyLinkedList,
    SinglyLinkedListNode,
)
from src.data_structures.linked_lists.linked_list_utilities import (
    MultipleElementsHandler,
    sort_list_multiple_elements_handlers,
)


class TestSinglyLinkedListModel:
    def test_initial_state(self):
        sll = SinglyLinkedList()
        assert sll.head is None
        assert sll.tail is None
        assert sll.size == 0
        assert sll.sll_initialized is False
        assert sll.sll_node is None


class TestSinglyLinkedListNode:
    def test_node_creation(self):
        node = SinglyLinkedListNode("data")
        assert node.data == "data"
        assert node.next is None


class TestMultipleElementsHandler:
    def test_handler_attributes(self):
        handler = MultipleElementsHandler(index=5, element="test")
        assert handler.index == 5
        assert handler.element == "test"


class TestSortedMultipleElementsHandlers:
    def test_sorting_by_index(self):
        handlers = [
            MultipleElementsHandler(3, "c"),
            MultipleElementsHandler(1, "a"),
            MultipleElementsHandler(2, "b"),
        ]

        sorted_handlers = sort_list_multiple_elements_handlers(handlers)
        sorted_indices = [h.index for h in sorted_handlers]
        assert sorted_indices == [1, 2, 3]
