import pytest
from src.data_structures.linked_lists.circular_singly_linked_list.circular_singly_linked_list import (
    CircularSinglyLinkedList,
)
from src.data_structures.linked_lists.circular_singly_linked_list.circular_singly_linked_list_operations import (
    initialize_csll,
    insert_csll_element,
    insert_csll_first_element,
    insert_csll_nth_element,
    get_element_at_index,
    delete_csll_first_element,
    delete_csll_last_element,
    delete_csll_nth_element,
    shallow_clear_singly_linked_list,
    deep_clear_singly_linked_list,
)


def test_initialize_and_basic_insertions():
    csll = CircularSinglyLinkedList()
    node1 = initialize_csll(csll, "start")
    assert csll.head == node1 and csll.tail == node1
    assert csll.size == 1
    node2 = insert_csll_element(csll, "second")
    assert csll.tail.data == "second"
    node3 = insert_csll_first_element(csll, "first")
    assert csll.head.data == "first"
    assert csll.size == 3


def test_insert_nth_element():
    csll = CircularSinglyLinkedList()
    initialize_csll(csll, "first")
    insert_csll_element(csll, "third")
    node = insert_csll_nth_element(csll, "second", 2)
    assert node.data == "second"
    assert csll.size == 3
    assert get_element_at_index(2, csll).data == "second"


def test_insert_nth_invalid():
    csll = CircularSinglyLinkedList()
    with pytest.raises(ValueError):
        insert_csll_nth_element(csll, "fail", 1)
    initialize_csll(csll, "first")
    with pytest.raises(IndexError):
        insert_csll_nth_element(csll, "fail", 5)


def test_get_element():
    csll = CircularSinglyLinkedList()
    initialize_csll(csll, "one")
    insert_csll_element(csll, "two")
    insert_csll_element(csll, "three")
    assert get_element_at_index(1, csll).data == "one"
    assert get_element_at_index(3, csll).data == "three"
    with pytest.raises(IndexError):
        get_element_at_index(4, csll)


def test_delete_elements():
    csll = CircularSinglyLinkedList()
    initialize_csll(csll, "one")
    insert_csll_element(csll, "two")
    insert_csll_element(csll, "three")
    delete_csll_nth_element(csll, 2)
    assert csll.size == 2
    deleted = delete_csll_last_element(csll)
    assert deleted.data == "three"
    deleted = delete_csll_first_element(csll)
    assert deleted.data == "one"
    assert csll.size == 0


def test_clear_operations():
    csll = CircularSinglyLinkedList()
    initialize_csll(csll, "one")
    insert_csll_element(csll, "two")
    shallow_clear_singly_linked_list(csll)
    assert csll.size == 0 and not csll.csll_initialized
    initialize_csll(csll, "reset")
    insert_csll_element(csll, "again")
    deep_clear_singly_linked_list(csll)
    assert csll.head is None and csll.tail is None and csll.size == 0
