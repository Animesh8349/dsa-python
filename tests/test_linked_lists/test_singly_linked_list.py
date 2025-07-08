"""
Unit tests for singly linked list implementation.
"""

import pytest
from data_structures.linked_lists.singly_linked_list import (
    SinglyLinkedList,
    SinglyLinkedListNode,
    initialize_sll,
    insert_sll_element,
    delete_sll_last_element,
)


class TestSinglyLinkedList:
    """Test cases for SinglyLinkedList class."""

    def test_create_empty_list(self):
        """Test creating an empty singly linked list."""
        sll = SinglyLinkedList()
        assert sll.head is None
        assert sll.tail is None
        assert sll.size == 0
        assert sll.sll_initialized is False

    def test_initialize_sll(self):
        """Test initializing a singly linked list with first element."""
        sll = SinglyLinkedList()
        node = initialize_sll(sll, "first")

        assert isinstance(node, SinglyLinkedListNode)
        assert node.data == "first"
        assert sll.head == node
        assert sll.tail == node
        assert sll.size == 1
        assert sll.sll_initialized is True

    def test_initialize_sll_with_none(self):
        """Test initializing with None should raise ValueError."""
        with pytest.raises(ValueError, match="Singly linked list cannot be None"):
            initialize_sll(None, "data")

    def test_insert_element_empty_list(self):
        """Test inserting element into empty list."""
        sll = SinglyLinkedList()
        result = insert_sll_element(sll, "first")

        assert result is True
        assert sll.size == 1
        assert sll.head.data == "first"
        assert sll.tail.data == "first"
        assert sll.sll_initialized is True

    def test_insert_multiple_elements(self):
        """Test inserting multiple elements."""
        sll = SinglyLinkedList()

        insert_sll_element(sll, "first")
        insert_sll_element(sll, "second")
        insert_sll_element(sll, "third")

        assert sll.size == 3
        assert sll.head.data == "first"
        assert sll.tail.data == "third"
        assert sll.head.next.data == "second"
        assert sll.head.next.next.data == "third"

    def test_delete_from_empty_list(self):
        """Test deleting from empty list returns None."""
        sll = SinglyLinkedList()
        result = delete_sll_last_element(sll)
        assert result is None

    def test_delete_single_element(self):
        """Test deleting single element from list."""
        sll = SinglyLinkedList()
        insert_sll_element(sll, "only")

        deleted = delete_sll_last_element(sll)

        assert deleted.data == "only"
        assert sll.head is None
        assert sll.tail is None
        assert sll.size == 0
        assert sll.sll_initialized is False

    def test_delete_multiple_elements(self):
        """Test deleting elements from list with multiple items."""
        sll = SinglyLinkedList()
        insert_sll_element(sll, "first")
        insert_sll_element(sll, "second")
        insert_sll_element(sll, "third")

        # Delete third element
        deleted = delete_sll_last_element(sll)
        assert deleted.data == "third"
        assert sll.size == 2
        assert sll.tail.data == "second"

        # Delete second element
        deleted = delete_sll_last_element(sll)
        assert deleted.data == "second"
        assert sll.size == 1
        assert sll.tail.data == "first"
        assert sll.head == sll.tail

    def test_delete_with_none_list(self):
        """Test deleting from None list raises ValueError."""
        with pytest.raises(ValueError, match="Singly linked list cannot be None"):
            delete_sll_last_element(None)

    def test_insert_with_none_list(self):
        """Test inserting into None list raises ValueError."""
        with pytest.raises(ValueError, match="Singly linked list cannot be None"):
            insert_sll_element(None, "data")
