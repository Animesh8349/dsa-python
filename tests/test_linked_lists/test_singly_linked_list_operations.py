"""
Unit tests for singly linked list operations.
"""

from data_structures.linked_lists.singly_linked_list.singly_linked_list import (
    SinglyLinkedList,
    SinglyLinkedListNode,
)
from data_structures.linked_lists.singly_linked_list.singly_linked_list_operations import (
    initialize_sll,
    insert_sll_element,
    delete_sll_last_element,
)


def test_initialize_singly_linked_list():
    """Test singly linked list initialization."""
    sll = SinglyLinkedList()
    result = initialize_sll(sll, "first")

    assert result is not None
    assert result.data == "first"
    assert sll.head is not None
    assert sll.head.data == "first"
    assert sll.tail == sll.head
    assert sll.size == 1
    assert sll.sll_initialized is True
    print("✓ Initialize SLL test passed")


def test_insert_elements():
    """Test inserting multiple elements."""
    sll = SinglyLinkedList()

    # Insert first element
    insert_sll_element(sll, "first")
    assert sll.size == 1
    assert sll.head.data == "first"
    assert sll.tail.data == "first"

    # Insert second element
    insert_sll_element(sll, "second")
    assert sll.size == 2
    assert sll.head.data == "first"
    assert sll.tail.data == "second"
    assert sll.head.next == sll.tail

    # Insert third element
    insert_sll_element(sll, "third")
    assert sll.size == 3
    assert sll.tail.data == "third"

    print("✓ Insert elements test passed")


def test_delete_last_element():
    """Test deleting the last element from the list."""
    singly_linked_list = SinglyLinkedList()

    # Test deletion from empty list
    result = delete_sll_last_element(singly_linked_list)
    assert result is None

    # Add elements and test deletion
    insert_sll_element(singly_linked_list, "first")
    insert_sll_element(singly_linked_list, "second")
    insert_sll_element(singly_linked_list, "third")

    # Delete last element
    deleted = delete_sll_last_element(singly_linked_list)
    assert deleted.data == "third"
    assert singly_linked_list.size == 2
    assert singly_linked_list.tail.data == "second"

    # Delete second-to-last element
    deleted = delete_sll_last_element(singly_linked_list)
    assert deleted.data == "second"
    assert singly_linked_list.size == 1
    assert singly_linked_list.tail.data == "first"
    assert singly_linked_list.head == singly_linked_list.tail

    # Delete last remaining element
    deleted = delete_sll_last_element(singly_linked_list)
    assert deleted.data == "first"
    assert singly_linked_list.size == 0
    assert singly_linked_list.head is None
    assert singly_linked_list.tail is None
    assert singly_linked_list.sll_initialized is False

    print("✓ Delete last element test passed")


def test_error_conditions():
    """Test error conditions."""
    try:
        initialize_sll(None, "data")
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert str(e) == "Singly linked list cannot be None"

    try:
        insert_sll_element(None, "data")
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert str(e) == "Singly linked list cannot be None"

    try:
        delete_sll_last_element(None)
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert str(e) == "Singly linked list cannot be None"

    print("✓ Error conditions test passed")


if __name__ == "__main__":
    test_initialize_singly_linked_list()
    test_insert_elements()
    test_delete_last_element()
    test_error_conditions()
    print("\n🎉 All tests passed!")
